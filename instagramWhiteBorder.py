import os
from PIL import Image
# Example usage
image_folder = ''  # Specify the folder containing your images | example: "C:/Users/[User]/Desktop/Images"
output_dir = ''  # Specify the output directory | example: "C:/Users/[User]/Desktop/ImagesWithLogo"
target_size = (1080, 1080)  # Square (1:1 aspect ratio)
aspect_ratio = "square"


def add_border(image_path, output_path, target_size, aspect_ratio):
    image = Image.open(image_path)

    # Calculate the dimensions based on the target size and aspect ratio
    width, height = target_size
    if aspect_ratio == "square":
        # Square (1:1 aspect ratio)
        if image.width > image.height:
            new_width = width
            new_height = int(width * (image.height / image.width))
        else:
            new_width = int(height * (image.width / image.height))
            new_height = height
    elif aspect_ratio == "portrait":
        # Portrait (4:5 aspect ratio)
        new_width = int(height * (image.width / image.height))
        new_height = height
    elif aspect_ratio == "landscape":
        # Landscape (16:9 aspect ratio)
        new_width = width
        new_height = int(width * (image.height / image.width))

    # Resize the image while maintaining its aspect ratio
    resized_image = image.resize((new_width, new_height))

    # Create a white background with the target size
    background = Image.new("RGB", target_size, (255, 255, 255))

    # Calculate the position to center the resized image on the white background
    x = (width - new_width) // 2
    y = (height - new_height) // 2

    # Paste the resized image onto the white background
    background.paste(resized_image, (x, y))

    # Save the image with the white border
    background.save(output_path)

def add_border_to_images(image_folder, output_dir, target_size, aspect_ratio):
    image_formats = ['.jpeg', '.gif', '.png', '.jpg']
    for filename in os.listdir(image_folder):
        file_extension = os.path.splitext(filename)[1].lower()

        if file_extension in image_formats:
            # Process image
            image_path = os.path.join(image_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '_border' + os.path.splitext(filename)[1]
            output_path = os.path.join(output_dir, output_filename)

            # Add white border to the image
            add_border(image_path, output_path, target_size, aspect_ratio)



add_border_to_images(image_folder, output_dir, target_size, aspect_ratio)
