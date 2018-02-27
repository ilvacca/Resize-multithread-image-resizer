import os
from PIL import Image
from resizeimage import resizeimage
import Tkinter, tkFileDialog
import re

root = Tkinter.Tk()
root.withdraw()
imagelist = []
c=0

filelist = tkFileDialog.askopenfilename(initialdir = "C:/",title = "Select photo folder",filetypes = (("JPEG files","*.jpg *.jpeg"),("PNG files","*.png"),("all files","*.*")),multiple=1)
path = os.path.dirname(filelist[0])+"/"
destination_folder=tkFileDialog.askdirectory(parent=root,initialdir=path,title='Destination directory')

destination_extention=raw_input("Destination extention [JPG,jpeg,png,bmp]: ")
if destination_extention == "":
    destination_extention = "jpg"
print "Found %d %s images in %s\n"%(len(imagelist),filelist[0].split(".")[-1],path)

w = int(raw_input("Height: "))
h = int(raw_input("Width: "))

for f in filelist:
    imagelist.append(f.replace(path,""))
                
for file in imagelist:
    c+=1
    with open(path+"/"+file, 'r+b') as f:
        with Image.open(f) as image:
            namefile = str(file[:-4])+'.'+destination_extention
            cover = resizeimage.resize_cover(image, [w, h])
            cover.save(destination_folder+"/"+namefile, image.format)
            print "%d/%d - Saved %s"%(c,len(imagelist),namefile)
