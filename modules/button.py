import Tkinter
from supports import actual_time

class button:

    def __init__(self,frame,inside_text,command,row,column,columnspan):

        # Structural properties
        self.frame = frame
        self.inside_text = inside_text
        self.command = command

        # Color properties
        self.bg = "#DDD"
        self.fg = "#151515"
        self.exc_bg = "#166139"
        self.exc_fg = "#C3FFC3"

        # Geometric properties
        self.row = row
        self.column = column
        self.pady = 6
        self.bd = 0
        self.width = 18
        self.columnspan = columnspan

        # Instancer
        self.button = Tkinter.Button(self.frame.frame,bg=self.bg,text=self.inside_text,command=self.command,pady=self.pady,width=self.width,bd=self.bd)
        self.button.grid(row=self.row,column=self.column,columnspan=self.columnspan)

    def is_clickable(self,b):
        if b == True:
            self.button.config(state="normal")
        elif b == False:
            self.button.config(state="disabled")

    def excited(self):
        self.button.config(bg=self.exc_bg,fg=self.exc_fg)
        
    def unexcited(self):
        self.button.config(bg=self.bg,fg=self.fg)
    
    def set_inner_text(self,text):
        self.button.config(text=text)

    def set_command(self,command):
        self.button.config(command=command)