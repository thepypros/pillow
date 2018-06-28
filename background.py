from PIL import Image

# Open the image and convert to RGBA mode
im = Image.open("promo.png")
im.convert("RGBA")
# Load the image data so we can manipulate pixel data
pixdata = im.load()

# For each row:
for y in range(im.height):
    # For each pixel in the row:
    for x in range(im.width):
        # Get the RGBA values
        r, g, b, a = im.getpixel((x, y))
        # If the pixel falls within our threshold of "green":
        if (g >= 70) and (g > r + 15) and (g > b + 15):
            # Make that pixel transparent
            pixdata[x, y] = (255, 255, 255, 0)
# Iterate through a second time to fix errors
for y in range(im.height):
    for x in range(im.width):
        # Need try/except, or code will break with an IndexError
        try:
            # If the pixels 5 to the left and right are transparent, I should be too!
            if (im.getpixel((x-5, y)) == (255, 255, 255, 0)) and (im.getpixel((x+5, y)) == (255, 255, 255, 0)):
                pixdata[x, y] = (255, 255, 255, 0)
        # The last pixel in a row wouldn't have an x+5 for example, so we'll catch the error here
        except IndexError:
            pass
# Optionally show the image
im.show()
