import Tkinter
from PIL import Image, ImageTk

class warningpanel:

    def __init__(self,parent,resolution_list):

        self.parent = parent
        self.resolutions_string = ""

        # Panel properties
        self.bg = "#202020"
        self.fg = "#CCC"
        self.pady = 30

        # Label properties
        self.font = ("Arial", 9, "normal")
        self.small_font = ("Arial", 7, "normal")
        self.font_small_fg = "#AAA"
        self.font_bg = self.bg
        self.font_fg = self.fg

        # Button Properties
        self.button_bg = "#b53438"
        self.button_padx = 15
        self.button_pady = 5

        # Panel Geometric properties
        self.warning_panel_width = 400
        self.warning_panel_height = 150
        self.centerX = int(((self.parent.winfo_screenwidth() / 2) - (self.warning_panel_width / 2)))
        self.centerY = int(((self.parent.winfo_screenheight() / 2) - (self.warning_panel_height / 2)))

        # Packing panel
        self.warningpanel = Tkinter.Toplevel(self.parent,pady=self.pady)
        self.warningpanel.title("RESIZE - Different images")
        self.warningpanel.geometry(
            "%sx%s+%s+%s" % (self.warning_panel_width, self.warning_panel_height, self.centerX, self.centerY))
        self.warningpanel.configure(background=self.bg)
        self.warningpanel.iconbitmap("images/Iconv1.ico")
        self.warningpanel.resizable(False, False)

        # Packing header
        self.img = Image.open("images/diff_resolution_v1.png").resize((91,70))
        self.image = ImageTk.PhotoImage(self.img)
        self.logo = Tkinter.Label(self.warningpanel, image=self.image, width=91,height=70, bd=0, bg=self.bg).pack(side="left",padx=8)

        # Packing text
        Tkinter.Label(self.warningpanel,text="Please select images with the same resolution.",font=self.font,bg=self.font_bg,fg=self.font_fg).pack()
        for i in resolution_list:
            self.resolutions_string += str(i)+" "
        self.resolutions_string+="..."
        Tkinter.Label(self.warningpanel, text="You selected: %s"%self.resolutions_string[:40],font=self.small_font,bg=self.font_bg, fg=self.font_small_fg).pack()


        # Packing button
        Tkinter.Button(self.warningpanel,text="Ok!",bg=self.button_bg,fg=self.fg,command=self.warningpanel.destroy,bd=0,padx=self.button_padx,pady=self.button_pady).pack(side="bottom",pady=5)

