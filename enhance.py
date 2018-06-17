from PIL import Image, ImageEnhance


def compare_enhancements(file, color_val, contrast_val, brightness_val, sharpness_val):
    im = Image.open(file)
    canvas = Image.new("RGB", (im.width*2, im.height*2), "white")
    original = im.resize((int(im.width/2), int(im.height/2)))
    color = ImageEnhance.Color(im)
    color_im = color.enhance(color_val)
    contrast = ImageEnhance.Contrast(im)
    contrast_im = contrast.enhance(contrast_val)
    brightness = ImageEnhance.Brightness(im)
    brightness_im = brightness.enhance(brightness_val)
    sharpness = ImageEnhance.Sharpness(im)
    sharpness_im = sharpness.enhance(sharpness_val)
    canvas.paste(color_im, (0, 0))
    canvas.paste(contrast_im, (im.width, 0))
    canvas.paste(brightness_im, (0, im.height))
    canvas.paste(sharpness_im, (im.width, im.height))
    canvas.paste(original, (int(canvas.width/2-original.width/2), int(canvas.height/2-original.height/2)))
    canvas.show()


compare_enhancements("girl.jpg", .5, .5, .5, .5)
compare_enhancements("girl.jpg", 2, 2, 2, 2)
