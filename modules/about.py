# coding=utf-8

import Tkinter
from PIL import Image, ImageTk
import datetime

class about_panel:

    def __init__(self,parent,version):

        self.parent = parent
        self.version_text_font = ("Arial", 7, "normal")
        self.version_text = "v.%s [%s]"%(str(version),datetime.datetime.now().strftime("%Y-%m-%d"))

        self.text_color = "#BBB"
        self.ver_fg = "#111"
        self.bg = "#202020"
        self.bg_b = "#B53438"

        self.header_width = 300
        self.header_height = 150

        self.header_text_a_pady=4
        self.version_text_pady = 0

        # Packing panel
        self.about_panel = Tkinter.Toplevel(self.parent)
        self.about_panel.title("RESIZE - About")
        self.about_panel.geometry("300x350")
        self.about_panel.configure(background=self.bg)
        self.about_panel.iconbitmap("images/Iconv1.ico")
        self.about_panel.resizable(False,False)

        # Packing header
        self.img = Image.open("images/about_header_v1.png").resize((self.header_width,self.header_height))
        self.image = ImageTk.PhotoImage(self.img)
        self.logo = Tkinter.Label(self.about_panel,image=self.image,width=self.header_width,height=self.header_height,bd=0,bg=self.bg)
        self.logo.pack()

        # Packing name
        self.img_name = Image.open("images/about_a_v1.png").resize((self.header_width, 75))
        self.image_name = ImageTk.PhotoImage(self.img_name)
        self.logo_name = Tkinter.Label(self.about_panel, image=self.image_name, width=self.header_width,bd=0)
        self.logo_name.pack()

        # Packing version
        self.version = Tkinter.Label(self.about_panel,font=self.version_text_font,text=self.version_text,fg=self.ver_fg,bg=self.bg_b,height=1,pady=self.version_text_pady)
        self.version.pack(fill="x")

        # Packing text
        text="\nAuthor: Alessio Vaccaro\n"
        text += "Blue Journey Astrophotography\n\n"
        text += "Email: alessio.vaccaro@outlook.it\n"
        #text+="Website: http://google.com\n"
        self.text = Tkinter.Label(self.about_panel,text=text,height=9,fg=self.text_color,bg=self.bg)
        self.text.pack()
