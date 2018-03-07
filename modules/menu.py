from options import option_panel

import Tkinter

class menu:

    def __init__(self,parent):
        self.parent = parent

        self.menubar = Tkinter.Menu(parent)
        #self.menubar.config(bg="red")

        self.filemenu = Tkinter.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Options", command=self.open_option_panel)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit")
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.helpmenu = Tkinter.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Help")
        self.helpmenu.add_command(label="About")
        self.menubar.add_cascade(label="?", menu=self.helpmenu)

        self.parent.config(menu=self.menubar)

    def open_option_panel(self):
        self.option = option_panel(self.parent)
        self.option.opt_panel.grab_set()
        self.option.opt_panel.after(50, lambda: self.option.opt_panel.focus_force())