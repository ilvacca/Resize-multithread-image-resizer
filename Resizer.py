from os import listdir
from PIL import Image
from resizeimage import resizeimage
import Tkinter, tkFileDialog
import re

root = Tkinter.Tk()
root.withdraw()
path = tkFileDialog.askdirectory(parent=root,initialdir="C:/Users/Alessio/Desktop/",title='Please select a directory')
destination_folder=tkFileDialog.askdirectory(parent=root,initialdir="C:/Users/Alessio/Desktop/",title='Destination directory')
destination_format=raw_input("Formato di destinazione [jpg]: ")

filelist = listdir(path)
w = int(raw_input("Larghezza: "))
h = int(raw_input("Altezza: "))
imagelist = []
c=0

for files in filelist:
    if type(re.search("(.png)$",files)) is not type(None):
        imagelist.append(files)
print "Found %d images"%(len(imagelist))
                
for file in imagelist:
    c+=1
    with open(path+"/"+file, 'r+b') as f:
        with Image.open(f) as image:
            namefile = str(file[:-4])+'.'+destination_format
            cover = resizeimage.resize_cover(image, [w, h])
            cover.save(destination_folder+"/"+namefile, image.format)
            print "%d/%d - Saved %s"%(c,len(imagelist),namefile)
 
