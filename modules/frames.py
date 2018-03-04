import Tkinter
from supports import *

selected_font = "Helvetica"

class frame:
    
    def __init__(self,root,bg,exc_bg,fg,exc_fg,exc_fg_num,fg_num,height,pady):
        self.bg = bg                    # Background
        self.fg = fg                    # Foreground (Testo)
        self.fg_num = fg_num            # Foreground (Numero)
        self.exc_bg = exc_bg            # Excited Background
        self.exc_fg = exc_fg            # Excited Forgroun (Testo)
        self.exc_fg_num = exc_fg_num    # Excited Foreground (Numero)
        self.height = height            # Altezza
        self.pady = pady

        self.frame = Tkinter.Frame(root,height=self.height,bg=self.bg,pady=self.pady)
        self.frame.pack(fill="x")

    def excited(self):
        self.frame.config(bg=self.exc_bg)

    def unexcited(self):
        self.frame.config(bg=self.bg)

class frame_number:
    
    def __init__(self,frame,number):
        self.frame = frame
        self.bg = self.frame.bg
        self.fg = self.frame.fg_num
        self.exc_bg = self.frame.exc_bg
        self.exc_fg = self.frame.exc_fg_num

        self.number = Tkinter.Label(self.frame.frame,text=number,bg=self.bg,fg=self.fg,font=(selected_font,30),padx=40)
        self.number.grid(row=0,column=0,rowspan=2)

    def excited(self):
        self.number.config(bg=self.exc_bg,fg=self.exc_fg)

    def unexcited(self):
        self.number.config(bg=self.bg,fg=self.fg)

class frame_text:

    def __init__(self,frame,text):
        self.frame = frame
        self.text = Tkinter.Label(frame.frame,text=text,bg=frame.bg,fg=frame.fg)
        self.text.grid(row=1,column=1)

    def set_text(self,text):
        self.text.config(text=text)

    def excited(self):
        self.text.config(bg=self.frame.exc_bg,fg=self.frame.exc_fg)

    def unexcited(self):
        self.text.config(bg=self.frame.bg,fg=self.frame.fg)
