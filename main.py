# coding=utf-8

from resizeimage import resizeimage
import os
from PIL import Image
import Tkinter
import tkFileDialog
import sys
sys.path.insert(0, "modules")

from header import header
from frames import frame, frame_number, frame_text, frame_menu
from options import option_panel
from about import about_panel
from logconsole import TraceConsole
from button import button, menu_button
from subframe import subframe
from entry import entry, entry_selector

class image_list:

    def __init__(self):
        """Inizializzazione della classe"""
        self.namelist=[]
        self.width_output=0
        self.listIsEmpty = True
        try:
            self.list = tkFileDialog.askopenfilename(initialdir = "C:/",title = "Select images",filetypes = (("PNG files","*.png"),("JPEG files","*.jpg *.jpeg"),("all files","*.*")),multiple=1)
            self.path = os.path.dirname(self.list[0])+"/"
            self.listIsEmpty = False
            for f in self.list:
                self.namelist.append(f.replace(self.path,""))
        except:
            self.listIsEmpty = True
            #print "%s - No images selected" % (actual_time())
        
    def set_destination_folder(self):
        self.destination_folder=tkFileDialog.askdirectory(parent=root,initialdir=self.path,title='Destination directory')
        #print "%s - Destination folder selected '%s'"%(actual_time(),self.destination_folder)

    def set_output_extension(self,ext):
        self.output_extension=ext
        if self.output_extension.lower() == ("" or "jpg" or "jpeg"):
            self.output_extension = "jpg"
        elif self.output_extension.lower() == ("png" or "PNG"):
            self.output_extension = "png"
        #print "%s - Destination ouput extension selected '%s'"%(actual_time(),self.output_extension)

    def set_resize_parameters(self,w_out,h_out):
        self.width_output = w_out
        self.height_output = h_out

    def resize_a_single_image(self,image_index,WW,HH,OutExt="jpg"):
        self.set_output_extension(OutExt)
        with open(self.path+"/"+self.namelist[image_index], 'r+b') as f:
            with Image.open(f) as image:
                namefile = str(self.namelist[image_index][:-4])+'.'+self.output_extension
                image = resizeimage.resize_cover(image.convert("RGB"), [WW, HH])
                image.save(self.destination_folder+"/"+namefile,"JPEG",quality=100)
                #print "%s - %d/%d - Saved %s" % (actual_time(),len(self.list),namefile)

    def resize(self):
        counter=0
        if self.width_output==0:
            self.set_resize_parameters()
            app.logger.log("")
        else:
            for file in self.namelist:
                counter+=1
                with open(self.path+"/"+file, 'r+b') as f:
                    with Image.open(f) as image:
                        namefile = str(file[:-4])+'.'+self.output_extension
                        image = resizeimage.resize_cover(image.convert("RGB"), [self.width_output, self.height_output])
                        image.save(self.destination_folder+"/"+namefile,"JPEG",quality=100)
                        #print "%s - %d/%d - Saved %s" % (actual_time(),counter,len(self.list),namefile)

class App:

    def __init__(self,root):

        """
        INITIALIZE "APP" OBJECT

        Keywords Argument:
            root = Tkinter object in which the App will be packed() = Tk.Tkinter()

        :type root: Tkinter object
        :param root:

        """

        # Tkinter properties
        root.title("RESIZE")
        self.root_width = 300
        self.root_height = 518
        self.centerX=((root.winfo_screenwidth()/2)-self.root_width/2)
        self.centerY =((root.winfo_screenheight()/2)-self.root_height/2)
        root.geometry("%sx%s+%s+%s"%(self.root_width,self.root_height,self.centerX,self.centerY))
        root.configure(background='#252525')
        root.iconbitmap("images/Iconv1.ico")
        root.resizable(False, False)                ################################# LEVARE COMMENTO IN FUTURO

        self.font = ("Arial",8)

        self.hasImageList = False
        self.hasOutputFolder = False
        self.image_list = False
        self.output_folder = None
        self.version = "0.55.03.8"

        self.geometry_method = Tkinter.StringVar()

        self.ready_to_resize = False
        self.oldW,self.oldH = None, None
        self.output_width, self.output_height = None, None
        self.check_for_changes = True

        self.menu = frame_menu(root, "#151515", 15)
        self.menu_button_options = menu_button(self.menu.frame,self.open_option_panel,"OPTIONS")
        self.menu_button_about = menu_button(self.menu.frame,self.open_about_panel, "ABOUT")
        self.menu_button_help = menu_button(self.menu.frame,None,"?")

    # HEADER ----------------------
        self.header = header(root,"images/Header1.png")

    # FRAME -----------------------
        self.frame1 = frame(root,"#151515","#1E824C","#6EDFA4","#4DAF7C","#282828",None)
        self.number1 = frame_number(self.frame1,"1")

        self.frame2 = frame(root,"#202020","#319B5C","#75EDAF","#58B283","#333333",None)
        self.number2 = frame_number(self.frame2,"2")

        self.frame3 = frame(root,"#242424","#42AD6E","#6EDFA4","#6EB892","#373737",None)
        self.number3 = frame_number(self.frame3,"3")

        self.button_select_images = button(self.frame1,"SELECT IMAGES",self.select_images,0,1,None)
        self.button_select_folder = button(self.frame2,"SELECT OUTPUT",self.select_folder,0,1,None)
        self.button_select_folder.is_clickable(False)

        self.text1 = frame_text(self.frame1,"Waiting for images...")
        self.text2 = frame_text(self.frame2,"Waiting for a folder...")

        self.subframe_frame3 = subframe(self.frame3)
        
        self.entry_selector_row1 = entry_selector(self.subframe_frame3.subframe,self.enable_widget_1,0,self.geometry_method,0,0,"W H")
        self.entry_W_row1 = entry(self.subframe_frame3.subframe,0,1)
        self.entry_H_row1 = entry(self.subframe_frame3.subframe,0,2)

        self.entry_selector_row2 = entry_selector(self.subframe_frame3.subframe,self.enable_widget_2,1,self.geometry_method,1,0,"W",)
        self.entry_W_row2 = entry(self.subframe_frame3.subframe,1,1)
        self.entry_H_row2 = entry(self.subframe_frame3.subframe,1,2)

        self.entry_selector_row3 = entry_selector(self.subframe_frame3.subframe,self.enable_widget_3,2,self.geometry_method,2,0,"H")
        self.entry_W_row3 = entry(self.subframe_frame3.subframe,2,1)
        self.entry_H_row3 = entry(self.subframe_frame3.subframe,2,2)

        self.button_start_resize = button(self.subframe_frame3.root, "START RESIZING", self.check_resize_values,4, 3, 3)
        self.button_start_resize.is_clickable(False)

        root.config(bd=0)

    # MENU ------------------------
        #self.menu = menu(root)

    # LOG
        self.logger = TraceConsole(root)
        self.logger.log("Welcome to RESIZƎ!")
        self.logger.log("Please select images to resize")

    # FOOTER FRAME ----------------

        self.footer = frame(root,"#D54A4E",None,None,None,None,5)

    # [MEGAPIXELS] -----

        #self.info_megapixel= Tkinter.Label(self.radioframe,text="",font=(selected_font,8),width=9,anchor="w",bg="#303030",fg="#ddd")
        #self.info_megapixel.grid(row=1,column=2,rowspan=2)

    # END [MEGAPIXELS] -----

    # Output geometry rows enablers

    def open_option_panel(self):
        self.option = option_panel(root)
        self.option.opt_panel.grab_set()
        self.option.opt_panel.after(50, lambda: self.option.opt_panel.focus_force())

    def open_about_panel(self):
        self.about = about_panel(root,self.version)
        self.about.about_panel.grab_set()
        self.about.about_panel.after(50, lambda: self.about.about_panel.focus_force())


    def empty_entries(self):
        self.entry_W_row1.entry.delete(0,Tkinter.END)
        self.entry_W_row1.entry.insert(0,"")
        self.entry_H_row1.entry.delete(0,Tkinter.END)
        self.entry_H_row1.entry.insert(0, "")
        self.entry_W_row2.entry.delete(0,Tkinter.END)
        self.entry_W_row2.entry.insert(0, "")
        self.entry_H_row2.entry.delete(0,Tkinter.END)
        self.entry_H_row2.entry.insert(0, "")
        self.entry_W_row3.entry.delete(0,Tkinter.END)
        self.entry_W_row3.entry.insert(0, "")
        self.entry_H_row3.entry.delete(0,Tkinter.END)
        self.entry_H_row3.entry.insert(0, "")

    def enable_widget_1(self):
        self.logger.log("Enter output Width and Height")
        self.entry_W_row1.set_state("normal")
        self.entry_H_row1.set_state("normal")
        self.entry_W_row2.set_state("disabled")
        self.entry_H_row3.set_state("disabled")

    def enable_widget_2(self):
        self.logger.log("Enter output Width")
        self.entry_selector_row1.set_state("normal")
        self.entry_W_row1.set_state("disabled")
        self.entry_H_row1.set_state("disabled")
        self.entry_W_row2.set_state("normal")
        self.entry_H_row3.set_state("disabled")

    def enable_widget_3(self):
        self.logger.log("Enter output Height")
        self.entry_selector_row1.set_state("normal")
        self.entry_W_row1.set_state("disabled")
        self.entry_H_row1.set_state("disabled")
        self.entry_W_row2.set_state("disabled")
        self.entry_H_row3.set_state("normal")

    def frame3_enable(self):
        self.geometry_method.set(0)
        self.entry_selector_row1.set_state("normal")
        self.entry_selector_row2.set_state("normal")
        self.entry_selector_row3.set_state("normal")
        self.button_start_resize.is_clickable(True)
        self.enable_widget_1()

    def frame3_disable(self):
        self.geometry_method.set(3)
        self.entry_selector_row1.set_state("disabled")
        self.entry_selector_row2.set_state("disabled")
        self.entry_selector_row3.set_state("disabled")
        self.entry_W_row1.set_state("disabled")
        self.entry_H_row1.set_state("disabled")
        self.entry_W_row2.set_state("disabled")
        self.entry_H_row3.set_state("disabled")
        self.button_start_resize.is_clickable(False)

    def frame2_excited(self,output_folder):
        self.button_select_images.set_inner_text("RESET WORKFLOW")
        self.button_select_folder.set_inner_text("RESET FOLDER")
        if len(output_folder)>19:
            self.text2.set_text(output_folder[:20] + "...")
        else:
            self.text2.set_text(output_folder[:20])
        self.button_select_folder.excited()
        self.frame2.excited()
        self.number2.excited()
        self.text2.excited()
        # Enabling Frame 3
        self.frame3_enable()

    def frame2_unexcited(self):
        self.button_select_folder.set_inner_text("SELECT FOLDER")
        self.text2.set_text("Select an output folder")
        self.output_folder = None
        self.button_select_folder.unexcited()
        self.frame2.unexcited()
        self.number2.unexcited()
        self.text2.unexcited()
        # Disabling Frame 3
        self.frame3_disable()

    def frame1_excited(self,number_of_images_in_list):
        self.button_select_images.set_inner_text("RESET IMAGE LIST")
        self.button_select_images.excited()
        self.frame1.excited()
        self.number1.excited()
        self.text1.excited()
        self.text1.set_text("Selected %s images"%number_of_images_in_list)
        self.button_select_folder.is_clickable(True)

    def frame1_unexcited(self):        
        self.image_list = False
        self.button_select_images.set_inner_text("SELECT IMAGES")
        self.button_select_images.unexcited()
        self.frame1.unexcited()
        self.number1.unexcited()
        self.text1.unexcited()
        self.text1.set_text("Select some images")
        self.button_select_folder.is_clickable(False)
        self.frame2_unexcited()
        self.frame3_disable()

    def select_images(self):
        if not self.image_list:
            self.image_list = image_list()
            if self.image_list.listIsEmpty:
                self.image_list = False
            elif self.image_list.listIsEmpty == False:
                self.frame1_excited(len(self.image_list.namelist))
        else:
            self.frame1_unexcited()

    def select_folder(self):
        # If output folder is not already setted try to set it
        if self.output_folder == None:
            # Call method to populate variable "self.output_folder"
            self.image_list.set_destination_folder()
            self.output_folder = self.image_list.destination_folder
            # If a non-zero-folder is set
            if len(self.output_folder) > 0:
                # Excite Frame 2 and go to Frame 3
                self.frame2_excited(self.output_folder)
            # Otherwise, if a zero-folder is set
            else:
                # Leave "self.output_folder" empty
                self.output_folder = None
        # Leave "self.output_folder" empty otherwise
        else:
            self.frame2_unexcited()

    def calculate_width_or_height(self,worh,dimension):
        if dimension == "w":
            return int(worh*2)
        elif dimension == "h":
            return int(worh/2)

    def check_resize_values(self):
        # If the resizing method is set to "WH"
        gm = int(self.geometry_method.get())

        if gm == 0:
            self.output_width = int(self.entry_W_row1.entry.get())
            self.output_height = int(self.entry_H_row1.entry.get())
        elif gm == 1:
            self.output_width = int(self.entry_W_row2.entry.get())
            self.output_height = self.calculate_width_or_height(int(self.output_width),"h")
        elif gm == 2:
            self.output_height = int(self.entry_H_row3.entry.get())
            self.output_width = self.calculate_width_or_height(int(self.output_height),"w")

        if (self.output_width == self.oldW) and (self.output_height == self.oldH):
            self.equals_dimensions = True
        else:
            self.equals_dimensions = False

        if self.ready_to_resize and self.equals_dimensions:
            self.button_start_resize.set_inner_text("START RESIZING")
            self.logger.log("Resizing [%sx%s]"%(self.output_width,self.output_height))
            self.ready_to_resize = False
            self.equals_dimensions = False
            self.oldW, self.oldH = None, None
            self.output_width, self.output_height = None, None
            self.empty_entries()

        elif (type(self.output_height)==int) and (type(self.output_width)==int):
            if (self.output_width > 0 ) and (self.output_height > 0):
                if (self.output_width == self.oldW) and (self.output_height ==  self.oldH):
                    self.button_start_resize.set_inner_text("RECLICK TO RESIZE")
                    self.logger.log("Reclick to resize to %sx%s!"%(self.output_width,self.output_height))
                    self.ready_to_resize = True
                elif (self.oldW == None) and (self.oldH == None):
                    self.button_start_resize.set_inner_text("RECLICK TO RESIZE")
                    self.logger.log("Reclick to resize to %sx%s!" % (self.output_width, self.output_height))
                    self.ready_to_resize = True
                else:
                    self.button_start_resize.set_inner_text("RECLICK TO CONFIRM")
                    self.logger.log("Are you ready? Reclick to confirm")
                    self.ready_to_resize = False

                self.oldW = self.output_width
                self.oldH = self.output_height

            else:
                print "Numeri non validi"
                self.ready_to_resize = False
        else:
            print "Numeri non validi"
            self.ready_to_resize = False

    ## OLD DEF BELOW

    def batch_resizer(self,W,H):
        self.logger.log("Resizing (%s/%s) %s"%(0+1,len(self.image_list.namelist),self.image_list.namelist[0]))
        self.image_list.resize_a_single_image(0,W,H)

    def select_output_directory(self):
        self.image_list.set_destination_folder()
        df = self.image_list.destination_folder
        self.ready_to_set_resizer_switcher(df)

root = Tkinter.Tk()
app = App(root)

root.mainloop()
