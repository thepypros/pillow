from PIL import Image
import argparse
import os

# For reference regarding image attributes and saving images
# im = Image.open("car.png")
# print(im.size, im.width, im.height)
# print(im.format, im.info)
# print(im.mode)
# im.save("car-new.bmp", "BMP")

# Description for our command line tool
text = "Use this tool to convert images."
# Instantiate parser
parser = argparse.ArgumentParser(description=text)
# Add arguments
parser.add_argument("-f", "--filename", help="Filename of image")
parser.add_argument("-e", "--extension", help="The file extension you want to convert to")
# Read arguments from the command line
args = parser.parse_args()
# Check to see if the user submitted a filename and extension
if args.filename and args.extension:
    # Try to convert the file
    try:
        # Create the new file name
        new_file = os.path.splitext(args.filename)[0] + args.extension
        print(new_file)
        # Open the existing file
        im = Image.open(args.filename)
        # If mode isn't RGB:
        if im.mode != "RGB":
            # Create a converted copy of the image
            output = im.convert("RGB")
            # Save new image
            output.save(new_file)
        # If the mode is already RGB:
        else:
            # Save new image
            im.save(new_file)
    # Throw an error message
    except IOError:
        print("Can't convert {}".format(args.filename))
