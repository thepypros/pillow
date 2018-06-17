from PIL import Image, ImageFilter


def compare_images(file, filter_object):
    im = Image.open(file)
    canvas = Image.new("RGB", (im.width*2, im.height))
    canvas.paste(im)
    effect = im.filter(filter_object)
    canvas.paste(effect, (im.width, 0))
    canvas.show()


# The filters listed below do not take any parameters - what you see is what you get:
# BLUR
# CONTOUR
# DETAIL
# EDGE_ENHANCE
# EDGE_ENHANCE_MORE
# EMBOSS
# FIND_EDGES
# SHARPEN
# SMOOTH
# SMOOTH_MORE

compare_images("bear.jpg", ImageFilter.GaussianBlur(radius=5))

# The filters listed below take one or more parameters and are documented here:
#   http://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html
# GaussianBlur(radius=2)
# BoxBlur(radius)
# UnsharpMask(radius=2, percent=150, threshold=3)
# Kernel(size, kernel, scale=None, offset=0)
# RankFilter(size, rank)
# MedianFilter(size=3)
# MaxFilter(size=3)
# ModeFilter(size=3)

# compare_images("bear.jpg", ImageFilter.BoxBlur(5))
