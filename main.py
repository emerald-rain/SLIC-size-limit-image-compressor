from PIL import Image
import os

def compress_images(input_folder, output_folder, max_size_kb):
    # Check the existence of the output folder
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get the list of files in the input folder with .png extension
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.png')]

    # Iterate through each image file in the input folder
    for image_file in image_files:
        # Set the input and output paths for the current image
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file.replace('.png', '.jpg'))

        # Open the image using the PIL library
        img = Image.open(input_path)

        # Save the image as .jpg with a quality level of 85 (JPEG compression)
        img.save(output_path, quality=85)

        # Check the file size after compression and reduce quality if necessary
        while os.path.getsize(output_path) > max_size_kb * 1024:
            img.save(output_path, quality=img.info['quality'] - 5)

if __name__ == "__main__":
    # User input for the paths and maximum size
    input_folder = input("Enter the path to the folder with .png images: ")
    output_folder = input("Enter the path to save .jpg images: ")
    max_size_kb = int(input("Enter the maximum size (in KB) for each image: "))

    # Call the function to compress images
    compress_images(input_folder, output_folder, max_size_kb)

    print("Process completed.")
