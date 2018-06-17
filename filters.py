from PIL import Image, ImageFilter


def compare_images(file, filter_object):
    im = Image.open(file)
    canvas = Image.new("RGB", (im.width*2, im.height))
    canvas.paste(im)
    effect = im.filter(filter_object)
    canvas.paste(effect, (im.width, 0))
    canvas.show()


compare_images("bear.jpg", ImageFilter.EMBOSS)

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

compare_images("bear.jpg", ImageFilter.BoxBlur(5))
