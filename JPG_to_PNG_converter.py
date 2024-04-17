import os
import sys
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print("Folder created")

for filename in os.listdir(image_folder):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{image_folder}/{filename}')
    img.save(f'{output_folder}/{clean_name}.png', 'PNG')
    print("Image saved")
