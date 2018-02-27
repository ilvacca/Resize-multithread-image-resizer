from os import listdir
from PIL import Image
from resizeimage import resizeimage
import Tkinter, tkFileDialog
import re

root = Tkinter.Tk()
root.withdraw()
imagelist = []
c=0

path = tkFileDialog.askdirectory(parent=root,initialdir="C:/Users/Alessio/Desktop/",title='Select photo folder')
destination_folder=tkFileDialog.askdirectory(parent=root,initialdir=path,title='Destination directory')

destination_extention=raw_input("Destination extention [JPG,jpeg,png,bmp]: ")
if destination_extention == "":
    destination_extention = "jpg"

filelist = listdir(path)
w = int(raw_input("Height: "))
h = int(raw_input("Width: "))

for files in filelist:
    if type(re.search("(.png)$",files)) is not type(None):
        imagelist.append(files)
print "Found %d %s images in %s\n"%(len(imagelist),destination_extention,path)
                
for file in imagelist:
    c+=1
    with open(path+"/"+file, 'r+b') as f:
        with Image.open(f) as image:
            namefile = str(file[:-4])+'.'+destination_extention
            cover = resizeimage.resize_cover(image, [w, h])
            cover.save(destination_folder+"/"+namefile, image.format)
            print "%d/%d - Saved %s"%(c,len(imagelist),namefile)
 
