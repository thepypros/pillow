from PIL import Image
# Open image
im = Image.open("logo.png")
print(im.size)
# Set height
new_height = 720
# Calculate new width, keeping ratio intact
new_width = int(new_height / im.height * im.width)
print(new_width)
#Resize to new dimensions
newsize = im.resize((new_width, new_height))

im.thumbnail((200, 200))
print(im.size)

im.save("logo.png")
