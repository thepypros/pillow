from PIL import Image, ImageFont, ImageDraw
from math import atan, degrees

# Open the source image and the logo image
im = Image.open("promo.png")
logo = Image.open("logo.png")
# Set the logo width to 10% of the source image width
new_width = int(.1 * im.width)
# Grab a resized logo with the thumbnail method
logo.thumbnail((new_width, new_width))
# Add some horizontal padding
x = int(im.width * .03)
# Add some vertical padding
y = im.height - int(im.height * .03) - logo.height
# Paste the logo on the source image with its new coordinates and a mask of itself
im.paste(logo, (x, y), logo)

# Create a new blank image in RGBA mode with identical dimensions to the source image
canvas = Image.new("RGBA", im.size)
# Create an instance of the ImageDraw class and pass in the new image
draw = ImageDraw.Draw(canvas)
# The string for our watermark
text = "COPYRIGHT"
# A new font object with font type and size
font = ImageFont.truetype("arial.ttf", size=200)
# The width and height of the specified text and font
text_width, text_height = draw.textsize(text, font)
# Calculate the length of the opposite and adjacent sides
opposite = im.height / 2
adjacent = im.width / 2
# Calculate the angle at which to rotate the watermark
text_angle = -degrees(atan(opposite/adjacent))
# The extra vertical space above the letters that needs to be accounted for for vertical centering
line_height = 36
# The number of pixels between the rectangle border and the text
padding = 50
# The (x, y) tuple to center the text
text_location = (im.width / 2 - text_width / 2, im.height / 2 - text_height / 2 - line_height / 2)
# The coordinates to position the rectangle around the text
x1 = text_location[0] - padding
y1 = text_location[1] - (padding - line_height)
x2 = text_location[0] + text_width + padding
y2 = text_location[1] + text_height + padding
# Draw the rectangle
draw.rectangle((x1, y1, x2, y2), outline=(255, 255, 255, 100))
# Draw the text
draw.text(text_location, text, font=font, fill=(255, 255, 255, 100))
# The new image object with the rotated watermark
rotated = canvas.rotate(text_angle)
# Paste the rotated watermark on the source image
im.paste(rotated, rotated)
# Optionally show the image
im.show()
