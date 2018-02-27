import os
from PIL import Image
from resizeimage import resizeimage
import Tkinter, tkFileDialog
import re

root = Tkinter.Tk()
root.withdraw()
imagelist = []
c=0

# Input module
filelist = tkFileDialog.askopenfilename(initialdir = "C:/",title = "Select photo folder",filetypes = (("JPEG files","*.jpg *.jpeg"),("PNG files","*.png"),("all files","*.*")),multiple=1)
path = os.path.dirname(filelist[0])+"/"
destination_folder=tkFileDialog.askdirectory(parent=root,initialdir=path,title='Destination directory')
print "Found %d %s images in %s\n"%(len(filelist),filelist[0].split(".")[-1],path)

# Select destination extention
destination_extention=raw_input("Destination extention [JPG,jpeg,png,bmp]: ")
if destination_extention == "":
    destination_extention = "jpg"

# Select output geometries
w = int(raw_input("Output height: "))
h = int(raw_input("Output width: "))

# Populate filename list
for f in filelist:
    imagelist.append(f.replace(path,""))

# Start conversion
for file in imagelist:
    c+=1
    with open(path+"/"+file, 'r+b') as f:
        with Image.open(f) as image:
            namefile = str(file[:-4])+'.'+destination_extention
            cover = resizeimage.resize_cover(image, [w, h])
            cover.save(destination_folder+"/"+namefile, image.format)
            print "%d/%d - Saved %s"%(c,len(imagelist),namefile)
