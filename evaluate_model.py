import tensorflow as tf
import os

# Configuration
image_size = (64, 64)
batch_size = 32
test_dir = 'output/geschirr/1_object_extraction_output/2_Baumstruktur_test/'
model_path = 'working/model/model_Geschirr.keras'

# Load model
model = tf.keras.models.load_model(model_path)

# Load test dataset
test_ds = tf.keras.utils.image_dataset_from_directory(
    test_dir,
    image_size=image_size,
    batch_size=batch_size,
    shuffle=False
)

# Evaluate
print("Evaluating on test set...")
results = model.evaluate(test_ds)
print(f"Test Loss: {results[0]:.4f}")
print(f"Test Accuracy: {results[1]:.4f}")
