from PIL import Image
from array import array


def image_to_pixels(image_path):
    # Open an image file
    image = Image.open(image_path)

    # Convert the image to a list of pixel values
    pixels = list(image.getdata())

    # If the image has multiple channels (e.g., RGB), flatten the list
    if image.mode == 'RGB':
        pixels = [pixel for channel in pixels for pixel in channel]

    return pixels




# Example usage
image_path = "C:/Edrive/projects/SimpleProjects/ImageCompressor/test.png"
pixels = image_to_pixels(image_path)


# Assuming your numbers are integers
numbers = array('i',pixels)

with open('textimage_array_numbers.bin', 'wb') as f:
    numbers.tofile(f)
