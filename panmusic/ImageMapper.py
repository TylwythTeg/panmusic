from Chord import *
from PIL import Image, ImageDraw

#Chord


class Pixel():
	def __init__(self):
		self.value = (127,243,180)
		self.bval = (125,125,125)


#img = Image.new("RGB", (962, 228), "white")


#s = (Pixel().value, Pixel().value, Pixel().value,Pixel().value, Pixel().bval, Pixel().bval, Pixel().bval, Pixel().bval)
#img.putdata(s)


draw = ImageDraw.Draw(img)
#draw.line((0, 0) + img.size)
#draw.line((0, img.size[1], img.size[0], 0), fill=128)
del draw






img.save("C:/Users/Rob/Pictures/Pillow Images/img1.png")