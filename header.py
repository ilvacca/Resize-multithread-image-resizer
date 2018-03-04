import Tkinter
from PIL import Image, ImageTk
from supports import *

class header:
    
    def __init__(self,root,h,w,photo_dir):
        self.root = root
        self.height = h
        self.width = w
        self.photo_dir = photo_dir
        self.img = Image.open("Header1.png").resize((self.width,self.height))
        self.image = ImageTk.PhotoImage(self.img) # 300,150
        self.header = Tkinter.Label(image=self.image,height=self.height,bd=0)  #140
        self.header.pack()