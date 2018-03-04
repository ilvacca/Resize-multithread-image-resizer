import Tkinter

class menu:

    def __init__(self,root):
        self.menubar = Tkinter.Menu(root)

        self.filemenu = Tkinter.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit")
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.helpmenu = Tkinter.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Help")
        self.helpmenu.add_command(label="About")
        self.menubar.add_cascade(label="?", menu=self.helpmenu)

        root.config(menu=self.menubar)