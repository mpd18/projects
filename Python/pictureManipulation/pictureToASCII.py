def getRow(int,stringList):
	i=0
	bounds=[36,72,108,144,180,216,256]
	for i in range(0,len(bounds)):
		if(int < bounds[i]):
			return i
			
def convertToGrey(RGB):
	return (RGB[0] + RGB[1] + RGB[2])/3

from PIL import Image, ImageFilter
import random
import sys
if(len(sys.argv) > 1):
	
	outfile = open("outfile.jpg","w");
	#Read image
	im = Image.open(sys.argv[1] )
	#resize image
	im = im.resize((512,255),Image.ANTIALIAS)
	im.save(outfile,"JPEG")

	greyscale = [
				" ",
				" ",
				".,-",
				"_ivc=!/|\\~",
				"gjez2]/(YL)t[+T7Vf",
				"mdK4ZGbNDXY5PQ",
				"W8KMA",
				"#%$"
				]
	string = ''
	textFile = open('picture.txt',"w")
	for y in range (0,im.size[1]):
		for x in range (0,im.size[0]):
			# subtract from 255 otherwise colors are inverted
			pixel = 255 - convertToGrey(im.getpixel((x,y)))
			row = getRow(pixel,greyscale)
			string += greyscale[row][random.randint(0,len(greyscale[row]) -1)]
		string +='\n'
		#write the string to the file line by line
		textFile.write(string)
		string = ''
	textFile.close()
else:
	print("no picture to convert")