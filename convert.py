from PIL import Image
import argparse
import os

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
        newfile = os.path.splitext(args.filename)[0] + args.extension
        print(newfile)
        # Open the file
        im = Image.open(args.filename)
        # If mode isn't RGB:
        if im.mode != "RGB":
            # Create a converted copy of the image
            output = im.convert("RGB")
            # Save new image
            output.save(newfile)
        else:
            # Save new image
            im.save(newfile)
    # Throw an error message
    except IOError:
        print("Can't convert {}".format(args.filename))
