
import matplotlib.pyplot as plt
import numpy as np
import os
from object_extraction import load_file, create_mask, fill_borders
from matplotlib.colors import rgb_to_hsv
from skimage.transform import resize

# Pfad zu Ihrem Bild (bitte anpassen falls anders)
img_path = 'data/input/geschirr/LOEFFEL_01_9547.jpg'

if not os.path.exists(img_path):
    # Fallback falls der Name anders ist
    import glob
    files = glob.glob('data/input/geschirr/*.jpg')
    if files: img_path = files[0]

if os.path.exists(img_path):
    print(f"Debugge Bild: {img_path}")
    im = load_file(img_path)
    pr = (225, 400)
    im_resized = (255*resize(im, pr)).astype('uint8')
    
    # Teste fill_borders mit Weiss
    fv = 255
    im_filled = fill_borders(im_resized, value_to_fill=fv, fraction_of_rows_to_remove=0.1, fraction_of_cols_to_remove=0.1)
    
    # Check HSV Values
    im_rgb = im_filled.astype(np.float32) / 255.0
    im_hsv = rgb_to_hsv(im_rgb) * np.array([255, 255, 255], dtype=np.float32)[None, None, :]
    
    v_channel = im_hsv[:,:,2]
    print(f"Helligkeit (Value) - Max: {np.max(v_channel):.1f}, Min: {np.min(v_channel):.1f}, Mittel: {np.mean(v_channel):.1f}")
    
    # Empfehlung fuer vth basierend auf dem Bild:
    # Wir wollen den Hintergrund (hell) ausschließen und das Messer (dunkel) einschließen.
    # Ein guter Schwellwert liegt oft knapp unter der Durchschnittshelligkeit.
    suggested_vth = -int(np.mean(v_channel) * 0.8)
    print(f"Vorschlag fuer vth: {suggested_vth}")

    # Teste Maske mit dem Vorschlag
    mask, _ = create_mask(im_resized, fraction_of_rows_to_remove=0.1, fraction_of_cols_to_remove=0.1, value_threshold=suggested_vth, value_to_fill=255)
    print(f"Pixel in Maske gefunden: {np.sum(mask)}")
else:
    print("Kein Bild gefunden in data/input/geschirr/*.jpg")
