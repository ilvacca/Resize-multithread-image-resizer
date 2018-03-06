import Tkinter

class entry_selector:
    
    #self.rb1 = Tkinter.Radiobutton(self.radioframe, text="W H",pady=3,font=(selected_font,9),\
    #        width=8,variable=self.geometry_method,value=0,state="disabled",command=self.enable_widget_1,indicatoron=0,bd=0,\
    #        background="#404040",activebackground="#F75C4C",selectcolor="#E74C3C")
    #self.rb1.grid(row=0,column=0,pady=2) 
    
    def __init__(self,root,value,variable,row,column,inner_text,initial_state,font_size,pady):
        self.root = root
        self.row = row
        self.column = column
        self.inner_text = inner_text
        self.initial_state = initial_state
        self.font_size = font_size
        self.width = 5
        self.pady = pady
        self.value = value
        self.variable = variable
        self.indicatoron = 0
        self.bd = 0
        self.background = "#404040"
        self.act_background = "#F75C4C"
        self.select_color = "#E74C3C"

        self.entry_selector = Tkinter.Radiobutton(self.root,text=self.inner_text,pady=self.pady,\
            value=self.value,variable=self.variable,state=self.initial_state,indicatoron=self.indicatoron,\
            command=None,background=self.background,activebackground=self.act_background,selectcolor=self.select_color,\
            bd=self.bd,width=self.width)
        self.entry_selector.grid(row=self.row,column=self.column,pady=1,sticky="we")

    def set_command(self,command):
        self.entry_selector.config(command=command)

class entry:
    
    #self.entryWidth_1 = Tkinter.Entry(self.radioframe,width=7,bd=0,\
    #            bg="#bbb",disabledbackground="#383838",disabledforeground="#505050",fg="#333",\
    #            insertbackground="orange",state="disabled")
    #self.entryWidth_1.grid(row=0,column=1,padx=2,ipady=4,sticky="e")

    # "entry" initialization
    def __init__(self,root,bg,dis_bg,fg,dis_fg,ins_bg,row,column,ipady):
        
        # Widget attributes
        self.bd = 0
        self.root = root
        self.bg = bg
        self.dis_bg = dis_bg
        self.fg = fg
        self.dis_fg = dis_fg
        self.insert_bg = ins_bg
        self.width = 7
        self.state = "disabled"

        # Grid packaging attributes
        self.row = row
        self.column = column
        self.padx = 1
        self.ipady = ipady
        self.sticky = "we"

        # Grid packaging
        self.entry = Tkinter.Entry(self.root,bg=self.bg,disabledbackground=self.dis_bg,\
            disabledforeground=self.dis_fg,fg=self.fg,insertbackground=self.insert_bg,\
            state=self.state,width=self.width,bd=self.bd)
        self.entry.grid(row=self.row,column=self.column,padx=self.padx,ipady=self.ipady,\
            sticky=self.sticky)

    def disabled_state(self):
        self.entry.config(state="disabled")

    def enabled_state(self):
        self.entry.config(state="normal")