# -------------------------------------------------
# -- Practical => Image Manipulation With Pillow --
# -------------------------------------------------

import os
from PIL import Image

print(os.getcwd())
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))

# Open The Image
myImage = Image.open("game.jpg")

# Show The Image
myImage.show()

# My Cropped Image
myBox = (10, 10, 150, 150)
myNewImage = myImage.crop(myBox)

# Show The New Image
myNewImage.show()

# My Converted Mode Image
myConverted = myImage.convert("L")
myConverted.show()
