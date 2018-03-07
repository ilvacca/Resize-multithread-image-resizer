import Tkinter
from supports import *

selected_font = "Helvetica"

class frame:

    def __init__(self,parent,bg,exc_bg,exc_fg,exc_fg_num,fg_num):

        # Structural properties
        self.root = parent

        # Color properties
        self.bg = bg                    # Background
        self.fg = "#AAA"                # Foreground (Testo)
        self.fg_num = fg_num            # Foreground (Numero)
        self.exc_bg = exc_bg            # Excited Background
        self.exc_fg = exc_fg            # Excited Forgroun (Testo)
        self.exc_fg_num = exc_fg_num    # Excited Foreground (Numero)

        # Geometric properties
        self.height = None              # Altezza
        self.pady = 10

        # Instancer
        self.frame = Tkinter.Frame(self.root,height=self.height,bg=self.bg,pady=self.pady)
        self.frame.pack(fill="x")

    def excited(self):
        self.frame.config(bg=self.exc_bg)

    def unexcited(self):
        self.frame.config(bg=self.bg)

class frame_number:

    def __init__(self,parent,number):

        # Structural properties
        self.frame = parent

        # Color properties
        self.bg = self.frame.bg
        self.fg = self.frame.fg_num
        self.exc_bg = self.frame.exc_bg
        self.exc_fg = self.frame.exc_fg_num

        # Geometric properties
        self.font_size = 30
        self.sticky = "ns"
        self.padx = 40
        self.row = 0
        self.column = 0
        self.rowspan = 5

        # Instancer
        self.number = Tkinter.Label(self.frame.frame,text=number,bg=self.bg,fg=self.fg,font=(selected_font,self.font_size),padx=self.padx)
        self.number.grid(row=self.row,column=self.column,rowspan=self.rowspan,sticky=self.sticky)

    def excited(self):
        self.number.config(bg=self.exc_bg,fg=self.exc_fg)

    def unexcited(self):
        self.number.config(bg=self.bg,fg=self.fg)

class frame_text:

    def __init__(self,parent,text):

        # Structural properties
        self.frame = parent

        # Geometric properties
        self.row = 1
        self.column = 1

        # Instancer
        self.text = Tkinter.Label(self.frame.frame,text=text,bg=self.frame.bg,fg=self.frame.fg)
        self.text.grid(row=self.row,column=self.column)

    def set_text(self,text):
        self.text.config(text=text)

    def excited(self):
        self.text.config(bg=self.frame.exc_bg,fg=self.frame.exc_fg)

    def unexcited(self):
        self.text.config(bg=self.frame.bg,fg=self.frame.fg)
