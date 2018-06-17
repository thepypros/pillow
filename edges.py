from PIL import Image

im = Image.open("promo.png")
im.convert("RGBA")
pixdata = im.load()

for y in range(im.height):
    for x in range(im.width):
        r, g, b, a = im.getpixel((x, y))
        if (g >= 70) and (g > r + 15) and (g > b + 15):
            pixdata[x, y] = (255, 255, 255, 0)
im.show()
for y in range(im.height):
    for x in range(im.width):
        try:
            if (im.getpixel((x-5, y)) == (255, 255, 255, 0)) and (im.getpixel((x+5, y)) == (255, 255, 255, 0)):
                pixdata[x, y] = (255, 255, 255, 0)
        except IndexError:
            pass
im.show()
