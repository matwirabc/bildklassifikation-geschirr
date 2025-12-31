
import os
import shutil
import glob

src_dir = 'output/geschirr/final_extraction/Ausschnitte/'
dst_base = 'media/geschirr_improved/train/'

classes = ['gabel-01', 'korkenzieher-01', 'loeffel-01', 'messer-01', 'trinkhalm-01']

for cls in classes:
    files = glob.glob(os.path.join(src_dir, f"{cls}_*.jpg"))
    for f in files:
        shutil.copy(f, os.path.join(dst_base, cls, os.path.basename(f)))
    print(f"Copied {len(files)} files for {cls}")
