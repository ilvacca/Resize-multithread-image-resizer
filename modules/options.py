import Tkinter
import ttk

class option_panel:

    def __init__(self,parent,output_extension):

        self.opt_panel = Tkinter.Toplevel(parent)
        self.opt_panel.title("Options")
        #self.opt_panel.geometry("450x200")     # REVIEW remove the comment
        self.opt_panel.configure(background='#202020')
        self.opt_panel.iconbitmap("images/Iconv1.ico")

        self.output_frame = output_option_frame(self.opt_panel)

        self.supported_extensions = output_extension
        self.compressions = [100,90,80,70,60,50,40,30,20,10]

        self.extension_card = output_single_card(self.output_frame.frame,0,0,"Format:","The output format desired.\nEXAMPLE: 'image_resized_01.jpg'",self.supported_extensions)
        self.quality_card = output_single_card(self.output_frame.frame,0,1,"Quality:","The output quality (0-100%).\nOnly applicable to JPEG outputs.",self.compressions)

        self.algorithm_frame = algorithm_option_frame(self.opt_panel)

        self.confirm_frame = confirm_option_frame(self.opt_panel,)# TODO it must takes extension_card and quality_card

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
        self.output_title_frame = Tkinter.Frame(self.parent,bg=self.title_bg,padx=12,pady=10)
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

    def __init__(self,parent,row,column,label,descr,list_items):

        self.bg = "#202020"
        self.label_font = ("AvenirNext LT Pro Bold",10)
        self.label_fg = "#DDD"

        self.description_font = ("AvenirNext LT Pro Regular", 8)
        self.description_fg = "#777"

        self.frame = Tkinter.Frame(parent,bg=self.bg,padx=5)
        self.frame.grid(row=row,column=column,padx=7)

        self.label = Tkinter.Label(self.frame,text=label,bg=self.bg,font=self.label_font,fg=self.label_fg)
        self.label.grid(row=0,column=0,sticky="w")

        self.combobox = ttk.Combobox(self.frame,values=list_items,height=5,width=8,background="red")
        self.combobox.current(0)
        self.combobox.grid(row=0,column=1)

        self.description = Tkinter.Label(self.frame,text=descr,fg=self.description_fg,font=self.description_font,bg=self.bg,width=28,anchor="w",justify="left",pady=10)
        self.description.grid(row=1,column=0,columnspan=2,sticky="w")

    def getValue(self):
        return self.combobox.get()

class algorithm_option_frame:

    def __init__(self, parent):

        # Structural properties
        self.selected_algorithm = 0
        self.parent = parent
        self.bg = "#202020"

        # Title properties
        self.title_bg = "#A12D2D"
        self.title_fg = "#FF4D52"
        self.title_font = ("AvenirNext LT Pro Bold", 18)

        # Algorithms buttons properties
        self.button_font = ("AvenirNext LT Pro Bold", 9)
        self.button_fg = "#DDD"
        self.button_width = 14
        self.button_height = 3

        # Description properties
        self.desc_font = ("AvenirNext LT Pro Regular", 8)
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
        self.description = Tkinter.Label(self.parent, bg=self.bg, fg=self.desc_fg, text="Lorem Ipsum",
                                         font=self.desc_font, justify="left", anchor="w", padx=13)
        self.description.pack(fill="x")


        # Packing Algorithm selectors
        # TODO Give those radiobuttons a command
        self.nneigh = Tkinter.Radiobutton(self.frame, width=self.button_width,
                                          height=self.button_height, font=self.button_font, value=0, variable=self.selected_algorithm ,
                                          text="Nearest\nNeighbor", bd=0, bg="#CC3D42", anchor="sw", indicatoron=0, fg=self.button_fg,
                                          padx=5, pady=5, justify="left")
        self.nneigh.pack(padx=5, side="left")

        self.blin = Tkinter.Radiobutton(self.frame, width=self.button_width, height=self.button_height,
                                        font=self.button_font, value=1, variable=self.selected_algorithm , text="Bilinear\nInterpolation",
                                        bd=0, bg="#992E31", anchor="sw", indicatoron=0, padx=5, pady=5, fg=self.button_fg, justify="left")
        self.blin.pack(padx=5, side="left")

        self.bicu = Tkinter.Radiobutton(self.frame, width=self.button_width, height=self.button_height,
                                        font=self.button_font, value=2, variable=self.selected_algorithm , text="Bicubic\nInterpolation", bd=0,
                                        bg="#732225", anchor="sw", indicatoron=0, padx=5, pady=5, fg=self.button_fg, justify="left")
        self.bicu.pack(padx=5, side="left")

        # Packing Spacer Frame
        self.footer_frame = Tkinter.Frame(self.parent, bg=self.bg, height=30)
        self.footer_frame.pack(fill="x")

class confirm_option_frame:

    def __init__(self,parent):

        self.cancel_bg = "red"
        self.ok_bg = "green"
        self.fg = "white"
        self.frame_bg = "#202020"
        self.parent = parent

        self.button_width = 10
        self.button_bg = "purple"
        self.button_fg = "white"

        self.frame = Tkinter.Frame(parent,bg=self.frame_bg,pady=10)
        self.frame.pack(fill="x")

        # TODO #37B Give to this button a working function
        self.ok_button = Tkinter.Button(self.frame,text="Save",width=self.button_width,bd=0,bg=self.ok_bg,fg=self.button_fg,command=self.ok)
        self.ok_button.grid(row=0,column=0)

        self.cancel_button = Tkinter.Button(self.frame,text="Cancel",width=self.button_width,bd=0,bg=self.button_bg,fg=self.button_fg,command=self.cancel)
        self.cancel_button.grid(row=0, column=1)

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

    def ok(self):
        stringasd = "ASD"
        print "Closing panel"
        self.parent.destroy()
        return stringasd

    def cancel(self):
        self.parent.destroy()
