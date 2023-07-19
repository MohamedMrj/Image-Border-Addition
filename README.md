
# Image Border Addition

This Python script allows you to add a white border to images, supporting various aspect ratios, and saves the processed images to a specified output directory. The script uses the Python Imaging Library (PIL) to handle image processing operations.

# Example:

## Before
![ezgif com-webp-to-jpg](https://github.com/MohamedMrj/Image-Border-Addition/assets/113178714/a9ef2bf5-4640-4fa3-9d16-287de9dc19b7)
![photo-1532463788086-56a492a0b34a](https://github.com/MohamedMrj/Image-Border-Addition/assets/113178714/05c96afb-ebb5-4ba4-b8f7-450ab04882f9)



## After
![ezgif com-webp-to-jpg_border](https://github.com/MohamedMrj/E-handel-hemsida/assets/113178714/f784d5b0-bf10-4efc-9188-4743057b60ef)
![photo-1532463788086-56a492a0b34a_border](https://github.com/MohamedMrj/E-handel-hemsida/assets/113178714/2489f0f0-3bc8-4cf0-899e-26f8e8db7ab1)

## Requirements

- Python 3.x
- Pillow (Python Imaging Library) - Install it using `pip install pillow`

## How to Use

1. Clone the repository or download the script file `add_border.py` to your local machine.

2. Install the required libraries using the following command (if not already installed):

   ```
   pip install pillow
   ```

3. Place the images you want to process in a folder.

4. Update the script with the paths to your image folder and the desired output directory, as well as the target size and aspect ratio settings. Open the script file and modify the following variables in the **Example usage** section:

   ```python
   image_folder = 'path/to/your/image/folder'  # Specify the folder containing your images
   output_dir = 'path/to/your/output/directory'  # Specify the output directory
   target_size = (1080, 1080)  # Square (1:1 aspect ratio)
   aspect_ratio = "square"
   ```

5. Run the script:

   ```
   python add_border.py
   ```

6. The script will process each image in the specified folder, add a white border according to the specified aspect ratio and target size, and save the processed images in the output directory with "_border" added to their filenames.

## Supported Image Formats

- JPEG (.jpeg, .jpg)
- GIF (.gif)
- PNG (.png)

Please ensure that your images are in one of the supported formats for the script to work correctly.

## License

This script is licensed under the [MIT License](LICENSE).

## Disclaimer

Please use this script responsibly and ensure that you have the necessary rights to process and modify the images in the specified folder. The author of this script is not responsible for any misuse or violation of copyrights.
