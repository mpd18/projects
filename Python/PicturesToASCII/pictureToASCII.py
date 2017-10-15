def getRow(int,stringList):
	i=0
	bounds=[36,72,108,144,180,216,252]
	for bound in bounds:
		if(int < bounds[i]):
			return i
		i+=1
def convertToGrey(RGB):
	return (RGB[0] + RGB[1] + RGB[2])/3

from PIL import Image, ImageFilter
import random
import sys
if(len(sys.argv) > 1):
	
	#Read image
	im = Image.open(sys.argv[1] )
	#Display image
	im = im.resize((512,256),Image.BILINEAR)
	#im = im.convert("L")

	greyscale = [
				" ",
				" ",
				".,-",
				"_ivc=!/|\\~",
				"gjez2]/(YL)t[+T7Vf",
				"mdK4ZGbNDXY5P*Q",
				"W8KMA",
				"#%$"
				]
	string = ''

	for y in range (0,im.size[1]):
		for x in range (0,im.size[0]):
			pixel = 255 - convertToGrey(im.getpixel((x,y)))
			row = getRow(pixel,greyscale)
			string += greyscale[row][random.randint(0,len(greyscale[row]) -1)]
		string +='\n'
	textFile = open('picture.txt',"w")
	textFile.write(string)
	textFile.close()
else:
	print("no picture to convert")
	
