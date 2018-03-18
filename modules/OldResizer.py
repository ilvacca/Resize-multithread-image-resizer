import os
from PIL import Image
from resizeimage import resizeimage
import Tkinter, tkFileDialog

root = Tkinter.Tk()
root.withdraw()
imagelist = []
c=0

# Input module
filelist = tkFileDialog.askopenfilename(initialdir = "C:/",title = "Select photo folder",filetypes = (("JPEG files","*.jpg *.jpeg"),("PNG files","*.png"),("all files","*.*")),multiple=1)
path = os.path.dirname(filelist[0])+"/"
destination_folder=tkFileDialog.askdirectory(parent=root,initialdir=path,title='Destination directory')
print "Found %d %s images in %s\n"%(len(filelist),filelist[0].split(".")[-1],path)

# Select output format
destination_extention=raw_input("Destination extention [JPG,jpeg,png,bmp]: ")
if destination_extention == "":
    destination_extention = "jpg"

# Select output geometries
#w = int(raw_input("Output width: "))
#h = int(raw_input("Output height: "))

# Populate filename list
for f in filelist:
    imagelist.append(f.replace(path,""))

# Start conversion
for file in imagelist:
    for filtro in [Image.NEAREST,Image.BILINEAR,Image.BICUBIC,Image.ANTIALIAS]:
        c+=1
        with open(path+"/"+file, 'r+b') as f:
            with Image.open(f) as image:
                resamplerate = 4
                w,h = image.size[0]/resamplerate, image.size[1]/resamplerate
                namefile = str(file[:-4])+str(filtro)+str(w)+'.'+destination_extention
                #cover = resizeimage.resize_cover(image,[w, h],filter=filtro)
                #cover = image.convert("RGB").resize((w,h),filtro)
                image = image.convert("RGB").resize((w,h))
                image.save(destination_folder+"/"+namefile, image.format)
                print "%d/%d - Saved %s"%(c,len(imagelist),namefile)
