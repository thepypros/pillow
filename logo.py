from PIL import Image, ImageFont, ImageDraw
from math import atan, degrees

im = Image.open("promo.png")
logo = Image.open("logo.png")
print(logo.size)
new_width = int(.1 * im.width)
logo.thumbnail((new_width, new_width))
x = int(im.width * .03)
y = im.height - int(im.height * .03) - logo.height
im.paste(logo, (x, y), logo)

im.show()

canvas = Image.new("RGBA", im.size)
draw = ImageDraw.Draw(canvas)

text = "COPYRIGHT"
font = ImageFont.truetype("arial.ttf", size=200)
text_width, text_height = draw.textsize(text, font)
print(text_width, text_height)
opposite = im.height / 2
adjacent = im.width / 2
text_angle = -degrees(atan(opposite/adjacent))

line_height = 36
padding = 50
text_location = (im.width / 2 - text_width / 2, im.height / 2 - text_height / 2 - line_height / 2)
x1 = text_location[0] - padding
y1 = text_location[1] - (padding - line_height)
x2 = text_location[0] + text_width + padding
y2 = text_location[1] + text_height + padding

draw.rectangle((x1, y1, x2, y2), outline=(255, 255, 255, 100))
draw.text(text_location, text, font=font, fill=(255, 255, 255, 100))

# Red guide lines to see text line height
# draw.line((0, im.height/2 - text_height/2 - 32, im.width, im.height/2 - text_height/2 -32 ), fill="Red")
# draw.line((0, im.height/2 + text_height, im.width, im.height/2 + text_height), fill="Red")
rotated = canvas.rotate(text_angle)
# rotated = canvas
im.paste(rotated, rotated)
im.show()
