import Tkinter

class option_panel:

    def __init__(self,parent):

        self.opt_panel = Tkinter.Toplevel(parent)
        self.opt_panel.title("Options")
        #self.opt_panel.geometry("450x200")
        self.opt_panel.configure(background='#202020')
        self.opt_panel.iconbitmap("images/Iconv1.ico")

        self.output_frame = output_option_frame(self.opt_panel)

        # TODO # REVIEW Everything below
        # ALGORITHM OPTIONS FRAME

        self.button_width = 40
        self.button_height = 2

        self.algorithm_frame = algorithm_option_frame(self.opt_panel)

        v=0

        self.nneigh = Tkinter.Radiobutton(self.algorithm_frame.frame,width=self.button_width,height=self.button_height,value=0,variable=v,text="Nearest\nNeighbor",bd=0,bg="#88B54B",anchor="w",indicatoron=0)
        self.nneigh.pack(side="left")

        self.blin = Tkinter.Radiobutton(self.algorithm_frame.frame,width=self.button_width,height=self.button_height,value=1,variable=v,text="Bilinear\nInterpolation",bd=0,bg="#464865",anchor="w",indicatoron=0)
        self.blin.pack(side="left")

        self.bicu = Tkinter.Radiobutton(self.algorithm_frame.frame,width=self.button_width,height=self.button_height,value=2, variable=v, text="Bicubic\nInterpolation",bd=0, bg="#D9A657", anchor="w", indicatoron=0)
        self.bicu.pack(side="left")

class output_option_frame:

    def __init__(self,parent):

        # Structural properties
        self.parent = parent

        # Packing
        self.frame = Tkinter.Frame(self.parent,bg="purple",height=150)
        self.frame.pack(fill="x")

class algorithm_option_frame:

    def __init__(self, parent):

        # Structural properties
        self.parent = parent

        # Packing
        self.frame = Tkinter.Frame(self.parent, bg="#303030",height=150)
        self.frame.pack(fill="x")
