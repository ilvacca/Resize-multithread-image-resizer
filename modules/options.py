import Tkinter
import ttk
import copy

class option_panel:

    def __init__(self,parent,output_extension,current_options):

        self.opt_panel = Tkinter.Toplevel(parent)
        self.opt_panel.title("Options")
        self.opt_panel.geometry("450x527")
        self.opt_panel.configure(background='#202020')
        self.opt_panel.iconbitmap("images/Iconv1.ico")
        self.parent = parent

        self.output_frame = output_option_frame(self.opt_panel)

        self.supported_extensions = output_extension
        self.compressions = [100,90,80,70,60,50,40,30,20,10]
        self.current_options = current_options
        self.new_options = self.current_options.copy()
        print "CURRENT:",self.current_options

        self.extension_card = output_single_card(self.output_frame.frame,0,0,"Format:","The output format desired.\nEXAMPLE: 'image_resized_01.jpg'",self.supported_extensions,"output",self.current_options,self.new_options)
        self.quality_card = output_single_card(self.output_frame.frame,0,1,"Quality:","The output quality (0-100%).\nOnly applicable to JPEG outputs.",self.compressions,"quality",self.current_options,self.new_options)

        self.algorithm_frame = algorithm_option_frame(self.opt_panel,self.current_options,self.new_options)

        self.confirm_frame = confirm_option_frame(self.opt_panel,self.current_options,self.new_options)# TODO it must takes extension_card and quality_card (?)

class output_option_frame:

    def __init__(self,parent):

        # Structural properties
        self.parent = parent
        self.bg = "#202020"

        # Title properties
        self.title_bg = "#A12D2D"
        self.title_fg = "#FF4D52"
        self.title_font = ("AvenirNext LT Pro Bold", 18)

        # Packing Title Frame
        self.output_title_frame = Tkinter.Frame(self.parent,bg=self.title_bg,padx=12,pady=8)
        self.output_title_frame.pack(fill="x")

        # Packing Title
        self.output_option_title = Tkinter.Label(self.output_title_frame,text="OUTPUT",font=self.title_font,anchor="w",bg=self.title_bg,fg=self.title_fg)
        self.output_option_title.pack(side="left")

        # Packing Frame
        self.frame = Tkinter.Frame(self.parent,bg=self.bg,height=150,padx=10,pady=25)
        self.frame.pack(fill="x")

        # Packing Spacer Frame
        self.footer_frame = Tkinter.Frame(self.parent, bg=self.bg, height=30)
        self.footer_frame.pack(fill="x")

class output_single_card:

    def __init__(self,parent,row,column,label,descr,list_items,option_to_be_set,current_options,new_options):

        self.bg = "#181818"
        self.label_font = ("AvenirNext LT Pro Bold",12)
        self.label_fg = "#DDD"
        self.new_options = new_options
        self.option_to_be_set = option_to_be_set

        self.description_font = ("Calibri", 9)
        self.description_fg = "#777"

        self.frame = Tkinter.Frame(parent,bg=self.bg,padx=7,pady=15)
        self.frame.grid(row=row,column=column,padx=7)

        self.label = Tkinter.Label(self.frame,text=label,bg=self.bg,font=self.label_font,fg=self.label_fg)
        self.label.grid(row=0,column=0,sticky="w")

        self.variabbile = Tkinter.StringVar(value=current_options[self.option_to_be_set])
        self.variabbile.trace('w', self.OptionCallBack)

        self.combobox_style = ttk.Style()
        self.combobox_style.configure("TCombobox", background = [('readonly', 'red')])
        self.combobox_style.configure("TCombobox", foreground=[('readonly', 'purple')])
        self.combobox = ttk.Combobox(self.frame,values=list_items,height=5,width=8,style="TCombobox",textvariable=self.variabbile)
        self.combobox['state'] = 'readonly'
        self.combobox.grid(row=0,column=1)

        self.description = Tkinter.Label(self.frame,text=descr,fg=self.description_fg,font=self.description_font,bg=self.bg,width=28,anchor="w",justify="left",pady=10)
        self.description.grid(row=1,column=0,columnspan=2,sticky="w")

    def OptionCallBack(self,*args):
        self.new_options[self.option_to_be_set] = self.combobox.get()

class algorithm_option_frame:

    def __init__(self,parent,current_options,new_options):

        # Structural properties
        self.current_options = current_options
        self.new_options = new_options
        self.selected_algorithm = self.new_options["resampling"]
        self.parent = parent
        self.bg = "#202020"

        if self.selected_algorithm == "NEAREST":
            self.selected_algorithm_v2 = Tkinter.IntVar(value=0)
        elif self.selected_algorithm == "BILINEAR":
            self.selected_algorithm_v2 = Tkinter.IntVar(value=1)
        elif self.selected_algorithm == "BICUBIC":
            self.selected_algorithm_v2 = Tkinter.IntVar(value=2)

        # Title properties
        self.title_bg = "#A12D2D"
        self.title_fg = "#FF4D52"
        self.title_font = ("AvenirNext LT Pro Bold", 18)

        # Algorithms buttons properties
        self.button_font = ("AvenirNext LT Pro Bold", 9)
        self.button_fg = "#DDD"
        self.button_width = 14
        self.button_height = 3
        self.button_active_background = "#404040"
        self.button_selected_background = "#CF844A"

        # Description properties
        self.desc_font = ("Calibri", 9)
        self.desc_fg = "#999"

        # Packing Title Frame
        self.algorithm_title_frame = Tkinter.Frame(self.parent,bg=self.title_bg,padx=12,pady=10)
        self.algorithm_title_frame.pack(fill="x")

        # Packing Title
        self.algorithm_option_title = Tkinter.Label(self.algorithm_title_frame,text="RESAMPLING ALGORITHM",font=self.title_font,anchor="w",bg=self.title_bg,fg=self.title_fg)
        self.algorithm_option_title.pack(side="left")

        # Packing Frame
        self.frame = Tkinter.Frame(self.parent,bg=self.bg,height=150,padx=10,pady=25)
        self.frame.pack(fill="x")

        # Packing Description
        description_text = "The resampling algorithm is the mathematical method used to reduce the\ndimensions of your photos. Nearest Neighbor (Default) is the simplest and\nfastest. Bilinear and Bicubic Interpolations are more accurate but slower."
        self.description = Tkinter.Label(self.parent, bg=self.bg, fg=self.desc_fg, text=description_text,
                                         font=self.desc_font, justify="left", anchor="w", padx=13)
        self.description.pack(fill="x")

        # Packing Algorithm selectors
        self.nneigh = Tkinter.Radiobutton(self.frame, width=self.button_width,
                                          height=self.button_height, font=self.button_font, value=0, variable=self.selected_algorithm_v2,
                                          text="Nearest\nNeighbor", bd=0, bg="#125A71", command=self.setValue, selectcolor=self.button_selected_background, activebackground=self.button_active_background, anchor="sw", indicatoron=0, fg=self.button_fg,
                                          padx=5, pady=5, justify="left")
        self.nneigh.pack(padx=5, side="left")

        self.blin = Tkinter.Radiobutton(self.frame, width=self.button_width, height=self.button_height,
                                        font=self.button_font, value=1, variable=self.selected_algorithm_v2, command=self.setValue, text="Bilinear\nInterpolation",
                                        bd=0, bg="#0E4759", activebackground=self.button_active_background, selectcolor=self.button_selected_background, anchor="sw", indicatoron=0, padx=5, pady=5, fg=self.button_fg, justify="left")
        self.blin.pack(padx=5, side="left")

        self.bicu = Tkinter.Radiobutton(self.frame, width=self.button_width, height=self.button_height,
                                        font=self.button_font, value=2, variable=self.selected_algorithm_v2, command=self.setValue, text="Bicubic\nInterpolation", bd=0,
                                        bg="#0C3D4D", activebackground=self.button_active_background, selectcolor=self.button_selected_background, anchor="sw", indicatoron=0, padx=5, pady=5, fg=self.button_fg, justify="left")
        self.bicu.pack(padx=5, side="left")

        # Packing Spacer Frame
        self.footer_frame = Tkinter.Frame(self.parent, bg=self.bg, height=30)
        self.footer_frame.pack(fill="x")

    def setValue(self):
        value = self.selected_algorithm_v2.get()
        if value == 0:
            self.new_options["resampling"] = "NEAREST"
        elif value == 1:
            self.new_options["resampling"] = "BILINEAR"
        elif value == 2:
            self.new_options["resampling"] = "BICUBIC"

        #self.selected_algorithm_v2.set(2)

class confirm_option_frame:

    def __init__(self,parent,current_options,new_options):

        self.cancel_bg = "red"
        self.ok_bg = "green"
        self.fg = "white"
        self.frame_bg = "#151515"
        self.parent = parent
        self.current_options = current_options
        self.new_options = new_options

        self.button_width = 10
        self.button_bg = "purple"
        self.button_fg = "white"

        self.frame = Tkinter.Frame(parent,bg=self.frame_bg,pady=10,padx=10)
        self.frame.pack(fill="x")

        self.cancel_button = Tkinter.Button(self.frame,text="Cancel",width=self.button_width,bd=0,bg="#B53438",fg=self.button_fg,command=self.cancel,pady=5)
        #self.cancel_button.grid(row=0, column=1)
        self.cancel_button.pack(side="right",padx=5)

        # TODO #37B Give to this button a working function
        self.ok_button = Tkinter.Button(self.frame,text="Save",width=self.button_width,bd=0,bg="#1E824C",fg=self.button_fg,command=self.ok,pady=5)
        #self.ok_button.grid(row=0,column=0)
        self.ok_button.pack(side="right")

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

    def ok(self):
        self.current_options["resampling"] = self.new_options["resampling"]
        self.current_options["output"] = self.new_options["output"]
        self.current_options["quality"] = self.new_options["quality"]
        print "SET:",self.current_options
        self.parent.destroy()

    def cancel(self):
        self.parent.destroy()
