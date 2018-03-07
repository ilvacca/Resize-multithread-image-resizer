import Tkinter
from PIL import Image, ImageTk
from supports import *

class header:
    
    def __init__(self,parent,photo_dir):

        # Structural properties
        self.root = parent
        self.photo_dir = photo_dir

        # Geometric properties
        self.height = 150
        self.width = 300
        self.bd = 0

        # Instancer
        self.img = Image.open(self.photo_dir).resize((self.width, self.height))
        self.image = ImageTk.PhotoImage(self.img)
        self.header = Tkinter.Label(image=self.image,height=self.height,bd=self.bd)  #140
        self.header.pack()