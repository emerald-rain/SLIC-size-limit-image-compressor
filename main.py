from PIL import Image
import os
from tqdm import tqdm

def compress_images(input_folder, output_folder, max_size_kb):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.png')]

    for image_file in tqdm(image_files, desc="Overall Progress", unit="photo"):
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file.replace('.png', '.jpg'))

        img = Image.open(input_path)

        for quality in tqdm(range(100, 0, -1), desc=f"Compression {image_file}", leave=False):
            img.save(output_path, quality=quality)

            if os.path.getsize(output_path) <= max_size_kb * 1024:
                break

if __name__ == "__main__":
    input_folder = input("Enter the path to the folder with .png images: ")
    output_folder = input("Enter the path to save .jpg images: ")
    max_size_kb = int(input("Enter the maximum size (in KB) for each image: "))

    compress_images(input_folder, output_folder, max_size_kb)

    print("Process completed.")
