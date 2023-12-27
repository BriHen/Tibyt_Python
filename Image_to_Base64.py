# Image_to_Base64.py

# This program is used to take a images from a folder and convert into Base 64 Format
# Lines of Base 64 format is saved in a text file to allow for later copy and paste
# Created to convert png files created by LibreSprite to create Tidbyt Gif apps
# BriHen 12/27/2023

import base64
import os

folder_of_images = "MarioandYoshi_imageset/"  # Where the imaged are located
text_file = "image_64.txt"  # The name of the text file where the base64 lines will be saved


# Function to take and image and convert into a base 64 string
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        # Read the image file in binary mode
        image_binary = image_file.read()

        # Encode the binary data into Base64
        base64_encoded = base64.b64encode(image_binary)

        # Convert the bytes to a string
        base64_string = base64_encoded.decode("utf-8")

        return base64_string


# Function to find all files in a folder
def images_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files
    except:
        print("Couldn't open folder path, remember to add a /")
        return []


# Start loop to take all images within folder, generate Base64, and append to text file
with open(text_file, 'w') as file:
    for image in images_in_folder(folder_of_images):
        png_image_path = folder_of_images + image
        base64_result = image_to_base64(png_image_path)
        file.write('"""' + base64_result + '""",' + "\n")  # Format was made for Pixlet format

print("Done, " + str(len(images_in_folder(folder_of_images))) + " images processed")
