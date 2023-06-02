import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
tallchars = "tlbfhkd"
botchars = "jgypq"
alphabet_images = {}

for char in characters:
    if char.islower():
        alphabet_images[char + "_lower"] = Image.open("Characters/" + char + "_lower.jpg")
    else:
        alphabet_images[char] = Image.open("Characters/" + char + ".jpg")

alphabet_images[" "] = Image.open("Characters/space.jpg")

# Define the dimensions of each alphabet image
alphabet_image_width_upper = 50
alphabet_image_height_upper = 50

alphabet_image_width_lower = 30
alphabet_image_height_lower = 30

# Define the spacing between each alphabet image
horizontal_spacing = 20
vertical_spacing = 10

# Calculate the dimensions of the final combined image
output_width = 2480
output_height = 3507

left_margin = 30
right_margin = 30
top_margin = 30
bottom_margin = 20

''' 
output_width = (alphabet_image_width_upper + horizontal_spacing) * len(user_text)
output_height = alphabet_image_height
'''
# Create a blank canvas for the combined image
combined_image = Image.new('RGB', (output_width, output_height), color='white')
draw = ImageDraw.Draw(combined_image)

# Iterate over each character in the user's input text

y_position = 50
# User input text
f = open("text.txt", "r")
lines = f.readlines()
for user_text in lines:
    x_position = 50
    sentence = user_text.split()
    for char in sentence:
        total = x_position
        for each_char in char:
            if each_char.islower():
                total += alphabet_image_width_lower + horizontal_spacing
            else:
                total += alphabet_image_width_upper + horizontal_spacing

        if total > 2430:  # limit to go to next line
            y_position += alphabet_image_height_upper + 50
            x_position = 50

        for each_char in char:
            lower = False
            tall = False
            bot = False
            digit = False

            if each_char.islower():
                if each_char in tallchars:
                    tall = True
                elif each_char in botchars:
                    bot = True
                each_char += "_lower"
                lower = True

            # Retrieve the corresponding alphabet image for the character
            alphabet_image = alphabet_images[each_char]

            if alphabet_image:
                # Resize the alphabet image to the desired dimensions
                if lower:
                    width = alphabet_image_width_lower

                    if tall or bot:
                        height = alphabet_image_height_upper
                    else:
                        height = alphabet_image_height_lower

                else:
                    width = alphabet_image_width_upper
                    height = alphabet_image_height_upper

                alphabet_image = alphabet_image.resize((width, height))

                # Paste the alphabet image onto the combined image
                if lower and not tall:
                    if bot:
                        combined_image.paste(alphabet_image, (x_position, y_position + 25))
                    else:
                        combined_image.paste(alphabet_image, (x_position, y_position + 15))
                else:
                    combined_image.paste(alphabet_image, (x_position, y_position))

                if lower:
                    horizontal_spacing = 5
                else:
                    horizontal_spacing = 10

            # Update the x-position for the next alphabet image
            x_position += width + horizontal_spacing

        x_position += 35

    y_position += (alphabet_image_height_upper + 50) * 2

# Display the combined image

combined_image.save("trial.png")
combined_image.show()

