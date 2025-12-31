import os
import subprocess
import glob

source_dir = '/Users/user/ws/py/imageclassify/data/input/geschirr'
pattern = os.path.join(source_dir, 'IMG_*.HEIC')
files = glob.glob(pattern)

print(f"Found {len(files)} HEIC files to convert.")

for f in files:
    filename = os.path.basename(f)
    # Extract XXXX from IMG_XXXX.HEIC
    num = filename.replace('IMG_', '').replace('.HEIC', '')
    target_filename = f"gabel-01_{num}.jpg"
    target_path = os.path.join(source_dir, target_filename)
    
    print(f"Converting {filename} -> {target_filename}")
    
    try:
        subprocess.run(['sips', '-s', 'format', 'jpeg', f, '--out', target_path], check=True, capture_output=True)
        # Remove original after successful conversion
        os.remove(f)
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert {filename}: {e.stderr.decode()}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

print("Conversion complete.")
