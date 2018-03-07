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

        self.has_option_panel = False

    def open_option_panel(self):
        o = my_option_panel(self.parent)
        o.top.grab_set()
        #self.parent.wait_window(o.top)
        #self.root.wait_window(o)
        #if self.has_option_panel == False:
         #   self.has_option_panel = True
         #   self.option_panel = option_panel()
        #else:
        #    self.option_panel.pack()

class option_panel:

    def __init__(self):
        #self.option_panel = Tkinter.Tk()

        top = self.top = Toplevel(parent)
        Label(top, text="Value").pack()

class my_option_panel:

    def __init__(self,parent):

        self.top = Tkinter.Toplevel(parent)
        self.top.title("Options")
        self.top.geometry("300x200")
        self.top.configure(background='#252525')
        self.top.iconbitmap("images/Iconv1.ico")

        Tkinter.Label(self.top, text="Value").pack()

        self.e = Tkinter.Entry(self.top)
        self.e.pack(padx=10)

        b = Tkinter.Button(self.top, text="OK", command=None)
        b.pack()
