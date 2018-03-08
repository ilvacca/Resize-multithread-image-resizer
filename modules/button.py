import Tkinter
from supports import actual_time

class button:

    def __init__(self,frame,inside_text,command,row,column,columnspan):

        # Structural properties
        self.frame = frame
        self.inside_text = inside_text
        self.command = command

        # Color properties
        self.bg = "#b53438"     # "#464f70" "#303A61" "#434e6b"
        self.fg = "#FFD0BF"        # "#222"
        self.exc_bg = "#166139"
        self.exc_fg = "#C3FFC3"
        self.act_bg = "#333"            # Clicking background
        self.dis_bg = "purple"
        self.dis_fg = "#6F2022"
        self.font = ("Arial",8,"bold")

        # Geometric properties
        self.row = row
        self.column = column
        self.pady = 6
        self.bd = 0
        self.width = 18
        self.columnspan = columnspan

        # Instancer
        self.button = Tkinter.Button(self.frame.frame,disabledforeground=self.dis_fg,activebackground=self.act_bg,fg=self.fg,bg=self.bg,text=self.inside_text,command=self.command,pady=self.pady,width=self.width,bd=self.bd,font=self.font)
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