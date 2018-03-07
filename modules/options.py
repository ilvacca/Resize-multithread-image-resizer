import Tkinter

class option_panel:

    def __init__(self,parent):

        self.opt_panel = Tkinter.Toplevel(parent)
        self.opt_panel.title("Options")
        self.opt_panel.geometry("300x200")
        self.opt_panel.configure(background='#252525')
        self.opt_panel.iconbitmap("images/Iconv1.ico")

        Tkinter.Label(self.opt_panel, text="Value").pack()

        self.e = Tkinter.Entry(self.opt_panel)
        self.e.pack(padx=10)

        b = Tkinter.Button(self.opt_panel, text="OK", command=None)
        b.pack()