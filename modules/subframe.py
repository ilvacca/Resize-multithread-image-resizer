#self.radioframe = Tkinter.Frame(self.geometries_frame,bg="#303030")
#        self.radioframe.grid(row=0,columnspan=4,column=2,rowspan=4)

import Tkinter

class subframe:

    def __init__(self,parent):

        # Structural properties
        self.root = parent

        # Color properties
        self.bg = self.root.bg
        self.exc_bg = self.root.exc_bg

        # Geometric properties
        self.height = None
        self.row = 0
        self.column = 2
        self.rowspan = 4
        self.columnspan = 4

        # Instancer
        self.subframe = Tkinter.Frame(self.root.frame,bg=self.bg,height=self.height)
        self.subframe.grid(row=self.row,columnspan=self.columnspan,column=self.columnspan,rowspan=self.rowspan)

    def excited(self):
        self.subframe.config(bg=self.exc_bg)

    def unexcited(self):
        self.subframe.config(bg=self.bg)