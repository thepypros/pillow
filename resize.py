from PIL import Image

# This file will let you test several methods. Feel free to uncomment sections you're working on.

# im = Image.open("fox.jpg")

# Resize with arbitrary dimensions
# new_size = im.resize((400,400))

# Calculate new_width by keeping a constant ratio
# new_height = 720
# new_width = int(new_height / im.height * im.width)
# new_size = im.resize((new_width, new_height))

# Not ideal to exceed original dimensions, but .resize will allow this
# too_large = im.resize((im.width*2, im.height*2))

# Thumbnail utilizes maximum dimensions and keeps constant ratio. Cannot return larger than original image
# im.thumbnail((2000, new_height))

# Rotate with the rotate method
# rotated = im.rotate(45, expand=False)
# print(rotated.size)
# rotated.show()

# Rotate with predefined options in transpose method
# rotated = im.transpose(Image.ROTATE_90)
# rotated = im.transpose(Image.ROTATE_270)

# Flip image horizontally or vertically
# flip_x = im.transpose(Image.FLIP_LEFT_RIGHT)
# flip_y = im.transpose(Image.FLIP_TOP_BOTTOM)

# Crop a 200x200 pixel from the center of a new image
im = Image.open("icecream.jpg")
xcenter = im.width / 2
ycenter = im.height / 2
x1 = xcenter - 100
y1 = ycenter - 100
x2 = xcenter + 100
y2 = ycenter + 100
cropped = im.crop((x1, y1, x2, y2))
