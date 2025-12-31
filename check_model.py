import tensorflow as tf
import os

model_path = 'working/model/model_Geschirr.keras'
if os.path.exists(model_path):
    model = tf.keras.models.load_model(model_path)
    print(f"Model Name: {model.name}")
    print(f"Output shape: {model.output_shape}")
    # Get the number of units in the last layer
    last_layer = model.layers[-1]
    print(f"Last layer units: {last_layer.units}")
else:
    print(f"Model file not found at {model_path}")
