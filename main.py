from PIL import Image
import os
from tqdm import tqdm

def compress_images(input_folder, output_folder, max_size_kb):
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # This function compresses all images from the input_folder to the output_folder. 
    # All images are saved in .jpg format. The quality of an image is gradually reduced 
    # until its size is less than the max_size_kb. 

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for image_file in tqdm(image_files, desc="Overall Progress", unit="photo"):
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file.replace('.png', '.jpg'))

        img = Image.open(input_path)

        img = img.convert('RGB')

        for quality in tqdm(range(100, 0, -1), desc=f"Compression {image_file}", leave=False):
            img.save(output_path, quality=quality)

            if os.path.getsize(output_path) <= max_size_kb * 1024:
                break

if __name__ == "__main__":
    ascii_art = """ 

 ░▒▓███████▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓██████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░        
 ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░        
       ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░        
       ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓██████▓▒░  
    Size Limiter for Image Compression\n
    """
    print(ascii_art)

    print("Specify the input and output data folders. \nPress Enter without providing any input to use the default folders `input_folder` and `output_folder`. \nIf these folders do not exist yet, they will be created after the first empty run.\n")

    input_folder = input("INPUT image folder path: ") or 'input_folder'
    output_folder = input("OTPUT image folder path: ") or 'output_folder'

    print("\nSpecify the maximum output image size. \nLeave the field blank for .jpg conversion with quality preservation, which can also reduce size.\n")
    max_size_kb = int(input("MAX size per image in KB: "))

    print()  # Add an empty line for spacing

    compress_images(input_folder, output_folder, max_size_kb)

    # Display summary
    input_folder_size = sum(os.path.getsize(os.path.join(input_folder, f)) for f in os.listdir(input_folder))
    output_folder_size = sum(os.path.getsize(os.path.join(output_folder, f)) for f in os.listdir(output_folder))

    print(f"\nSummary:")
    print(f"Input folder size: {input_folder_size / (1024 * 1024):.2f} MB")
    print(f"Output folder size: {output_folder_size / (1024 * 1024):.2f} MB")

    # Wait for Enter key press
    input("\nPress Enter to exit.")
