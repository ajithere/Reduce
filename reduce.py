import os,sys
import PIL
from PIL import Image

if len(sys.argv) == 3:
	path = sys.argv[1]
	outpath = sys.argv[2]
elif len(sys.argv) == 1:
	path = "./source/"
	outpath = "./destination"
else:
	print "Invaild entries..."
	 

for filename in os.listdir(path):
	print "Reducing size of " + filename
	basewidth = 1024
	img = Image.open(path + "/" + filename)
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
	img.save(outpath + "/" + filename)
	print "Successfully converted"
