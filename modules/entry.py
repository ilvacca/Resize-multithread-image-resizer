import Tkinter

class entry_selector:

    def __init__(self,root,command,value,variable,row,column,inner_text):

        # Structural properties
        self.root = root
        self.row = row
        self.column = column
        self.inner_text = inner_text
        self.initial_state = "disabled"
        self.command = command

        # Color properties
        self.font = ("Arial", 8, "bold")
        self.background = "#404040"
        self.act_background = "#F75C4C"
        self.select_color = "#E74C3C"
        self.fg = "#CCC"

        # Geometric properties
        self.width = 5
        self.pady = 3
        self.value = value
        self.variable = variable
        self.indicatoron = 0
        self.bd = 0

        self.entry_selector = Tkinter.Radiobutton(self.root,text=self.inner_text,pady=self.pady,value=self.value,variable=self.variable,state=self.initial_state,indicatoron=self.indicatoron,\
            command=self.command,background=self.background,activebackground=self.act_background,selectcolor=self.select_color,\
            bd=self.bd,width=self.width,font=self.font,fg=self.fg)
        self.entry_selector.grid(row=self.row,column=self.column,pady=1,sticky="we")

    def set_command(self,command):
        self.entry_selector.config(command=command)

    def is_clickable(self,b):
        if b == True:
            self.entry_selector.config(state="normal")
        elif b == False:
            self.entry_selector.config(state="disabled")

    def set_state(self,state):
        if state.lower() == "disabled":
            self.entry_selector.config(state="disabled")
        elif state.lower() == "active":
            self.entry_selector.config(state="active")
        elif state.lower() == "normal":
            self.entry_selector.config(state="normal")

class entry:

    def __init__(self,root,row,column):

        # Structural properties
        self.root = root
        self.state = "disabled"

        # Color properties
        self.bg = "#606060"
        self.dis_bg = "#202020"
        self.fg = "#F75C4C"
        self.dis_fg = "#202020"
        self.insert_bg = "#F75C4C"

        # Geometric properties
        self.bd = 0
        self.width = 7
        self.row = row
        self.column = column
        self.padx = 1
        self.ipady = 4
        self.sticky = "we"
        self.justify = "center"

        # Instancer
        self.entry = Tkinter.Entry(self.root,bg=self.bg,disabledbackground=self.dis_bg,\
            disabledforeground=self.dis_fg,fg=self.fg,insertbackground=self.insert_bg,\
            state=self.state,width=self.width,bd=self.bd,justify=self.justify)
        self.entry.grid(row=self.row,column=self.column,padx=self.padx,ipady=self.ipady,\
            sticky=self.sticky)

    def set_state(self,state):
        if state.lower() == "disabled":
            self.entry.config(state="disabled")
        elif state.lower() == "normal":
            self.entry.config(state="normal")

    def is_clickable(self,b):
        if b == True:
            self.entry.config(state="normal")
        elif b == False:
            self.entry.config(state="disabled")