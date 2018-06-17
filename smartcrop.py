from PIL import Image, ImageFilter
from numpy import mean, std

# Open image
im = Image.open("cat.png")
# Find edges of image
edge = im.filter(ImageFilter.FIND_EDGES)
# Create list to store edge pixels
edgedata = []

# For each row of pixels
for y in range(edge.height):
    # For each pixel in the row
    for x in range(edge.width):
        # Get the RGBA channel data
        r, g, b = edge.getpixel((x, y))
        # If a pixel is "almost black" or it's near the edge of the image:
        if (r < 20 and g < 20 and b < 20) or (x < 5 or x > edge.width - 5) or (y < 5 or y > edge.height - 5):
            pass
        else:
            # Add the x,y coordinate of the edge pixel to the edgedata list
            edgedata.append((x, y))


def remove_outliers(data, number_of_devs):
    data_mean = mean(data)
    data_std = std(data)
    cut_off = data_std * number_of_devs
    lower_limit = data_mean - cut_off
    upper_limit = data_mean + cut_off
    data_without_outliers = [i for i in data if lower_limit <= i <= upper_limit]
    return data_without_outliers


xdata = [i[0] for i in edgedata]
x = remove_outliers(xdata, 2.5)
ydata = [i[1] for i in edgedata]
y = remove_outliers(ydata, 2.5)

x1 = min(x)
y1 = min(y)
x2 = max(x)
y2 = edge.height

# x1 = x[0]
# y1 = y[0]
# x2= x[1]


print(x1, y1, x2, y2)
cropped = im.crop((x1, y1, x2, y2))
cropped.show()
