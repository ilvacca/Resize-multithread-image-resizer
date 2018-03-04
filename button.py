import Tkinter

class button:
    
    #self.select_images = Tkinter.Button(self.frame_select_images,text="Select Images",\
        #command=self.select_images,pady=6,width=18,bd=0)
    #self.select_images.grid(row=0,column=1)

    def __init__(self,frame,inside_text,command,bg,fg,exc_bg,exc_fg,row,column,pady,width,bd):
        self.frame = frame
        self.inside_text = inside_text
        self.bg = bg
        self.fg = fg
        self.exc_bg = exc_bg
        self.exc_fg = exc_fg
        self.command = command

        self.button = Tkinter.Button(self.frame.frame,text=self.inside_text,command=self.command,pady=pady,width=width,bd=bd)
        self.button.grid(row=row,column=column)

    def excited(self):
        self.button.config(bg=self.exc_bg,fg=self.exc_fg)
        
    def unexcited(self):
        self.button.config(bg=self.bg,fg=self.fg)