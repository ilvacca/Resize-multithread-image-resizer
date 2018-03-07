# coding=utf-8

from resizeimage import resizeimage
import os
from PIL import Image
import Tkinter
import tkFileDialog
import sys
sys.path.insert(0, "modules")

from header import header
from menu import menu
from frames import frame, frame_number, frame_text
from logconsole import TraceConsole
from button import button
from subframe import subframe
from entry import entry, entry_selector
from supports import actual_time

selected_font = "Helvetica"

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

        :param root:

        """

        # Tkinter properties
        root.title("RESIZE")
        root.geometry("300x520")
        root.configure(background='#252525')
        root.iconbitmap("images/Iconv1.ico")
        #root.resizable(False, False)                ################################# LEVARE COMMENTO IN FUTURO

        self.hasImageList = False
        self.hasOutputFolder = False
        self.image_list = False
        self.output_folder = None

        self.geometry_method = 0

        self.ready_to_resize = False
        self.oldW,self.oldH = 0,0

    # HEADER ----------------------
        self.header = header(root,"images/Header1.png")

    # FRAME -----------------------
        self.frame1 = frame(root,"#151515","#1E824C","#6EDFA4","#4DAF7C","#252525")
        self.number1 = frame_number(self.frame1,"1")

        self.frame2 = frame(root,"#202020","#319B5C","#75EDAF","#58B283","#303030")
        self.number2 = frame_number(self.frame2,"2")

        self.frame3 = frame(root,"#242424","#42AD6E","#6EDFA4","#6EB892","#343434")
        self.number3 = frame_number(self.frame3,"3")

        self.button_select_images = button(self.frame1,"Select images",self.select_images,0,1,None)
        self.button_select_folder = button(self.frame2,"Select output folder",self.select_folder,0,1,None)
        self.button_select_folder.is_clickable(False)
        # SET INNER TEXT EXAMPLE: self.button_select_images.set_inner_text("Click to Reset")

        self.text1 = frame_text(self.frame1,"Select some images")
        self.text2 = frame_text(self.frame2,"Select an output folder")

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

        self.button_start_resize = button(self.subframe_frame3.root, "Start resizing", self.check_resize_values,4, 3, 3)
        self.button_start_resize.is_clickable(False)

        root.config(bd=0)

    # MENU ------------------------
        self.menu = menu(root)

    # LOG
        self.logger = TraceConsole(root)
        self.logger.log("Welcome to RESIZƎ!")
        self.logger.log("Please select images to resize")



    # [RESIZER] ------
        #self.start_resizing = Tkinter.Button(self.geometries_frame,text="Resize!",command=self.resize,pady=6,state="disabled",width=17,bd=0)
        #self.start_resizing.grid(row=5,column=2,ipadx=5,sticky=Tkinter.W)
    # END [RESIZER] ------

    # [MEGAPIXELS] -----

        #self.info_megapixel= Tkinter.Label(self.radioframe,text="",font=(selected_font,8),width=9,anchor="w",bg="#303030",fg="#ddd")
        #self.info_megapixel.grid(row=1,column=2,rowspan=2)

    # END [MEGAPIXELS] -----

    # Output geometry rows enablers

    def enable_widget_1(self):
        self.logger.log("Enter output Width and Height")
        self.geometry_method = 0
        self.entry_W_row1.set_state("normal")
        self.entry_H_row1.set_state("normal")
        self.entry_W_row2.set_state("disabled")
        self.entry_H_row3.set_state("disabled")

    def enable_widget_2(self):
        self.logger.log("Enter output Width")
        self.geometry_method = 1
        self.entry_selector_row1.set_state("normal")
        self.entry_W_row1.set_state("disabled")
        self.entry_H_row1.set_state("disabled")
        self.entry_W_row2.set_state("normal")
        self.entry_H_row3.set_state("disabled")

    def enable_widget_3(self):
        self.logger.log("Enter output Height")
        self.geometry_method = 2
        self.entry_selector_row1.set_state("normal")
        self.entry_W_row1.set_state("disabled")
        self.entry_H_row1.set_state("disabled")
        self.entry_W_row2.set_state("disabled")
        self.entry_H_row3.set_state("normal")

    def frame3_enable(self):
        self.entry_selector_row1.set_state("active")
        self.entry_selector_row2.set_state("normal")
        self.entry_selector_row3.set_state("normal")
        self.button_start_resize.is_clickable(True)
        self.enable_widget_1()

    def frame3_disable(self):
        print "Disable Frame 3"
        self.entry_selector_row1.set_state("disabled")
        self.entry_selector_row2.set_state("disabled")
        self.entry_selector_row3.set_state("disabled")
        self.entry_W_row1.set_state("disabled")
        self.entry_H_row1.set_state("disabled")
        self.entry_W_row2.set_state("disabled")
        self.entry_H_row3.set_state("disabled")
        self.button_start_resize.is_clickable(False)

    def frame2_excited(self,output_folder):
        self.button_select_images.set_inner_text("Reset workflow")
        self.button_select_folder.set_inner_text("Reset folder")
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
        self.button_select_folder.set_inner_text("Select output folder")
        self.text2.set_text("Select an output folder")
        self.output_folder = None
        self.button_select_folder.unexcited()
        self.frame2.unexcited()
        self.number2.unexcited()
        self.text2.unexcited()
        # Disabling Frame 3
        self.frame3_disable()

    def frame1_excited(self,number_of_images_in_list):
        self.button_select_images.set_inner_text("Reset image list")
        self.button_select_images.excited()
        self.frame1.excited()
        self.number1.excited()
        self.text1.excited()
        self.text1.set_text("Selected %s images"%number_of_images_in_list)
        self.button_select_folder.is_clickable(True)

    def frame1_unexcited(self):        
        self.image_list = False
        self.button_select_images.set_inner_text("Select images")
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
        if self.geometry_method == 0:
            self.output_width = self.entry_W_row1.entry.get()
            self.output_height = self.entry_H_row1.entry.get()
        elif self.geometry_method == 1:
            self.output_width = self.entry_W_row2.entry.get()
            self.output_height = self.calculate_width_or_height(int(self.output_width),"h")
        elif self.geometry_method == 2:
            self.output_height = self.entry_H_row3.entry.get()
            self.output_width = self.calculate_width_or_height(int(self.output_height),"w")
        print self.output_width, self.output_height

    #def read_resize_values(self):
    
    ## OLD DEF BELOW

    def ready_to_choose_folder_switcher(self,list):
        if len(list) > 0:
            self.logger.log("Found %d images. Select an output folder"%(len(list)))
            self.select_images.config(text="Change Images")
            self.images_found_text.config(text=("%s images selected"%(len(self.image_list.list))))
            self.frame_number_1.config(fg=self.excited_frame1_foreground,bg=self.excited_frame1_background)
            self.frame_select_images.config(bg=self.excited_frame1_background)
            self.images_found_text.config(fg=self.excited_frame1_foreground,bg=self.excited_frame1_background)
            
            self.select_output_directory.config(state="normal")
        else:
            self.image_list=[]
            self.logger.log("Image list cleared")
            self.logger.log("Please select images to resize")
            self.select_images.config(text="Select Images")
            self.select_output_directory.config(bg="white",state="disabled")
            self.start_resizing.config(state="disabled")

            self.frame_number_1.config(fg="#252525",bg=self.frame1_background)
            self.frame_select_images.config(bg=self.frame1_background)
            self.images_found_text.config(text=("Select some images first"),fg=self.frame1_foreground,bg=self.frame1_background)

            self.frame_number_2.config(bg=self.frame2_background,fg=self.frame2_number_foreground)
            self.frame_folder_selector.config(bg=self.frame2_background)
            self.output_folder_text.config(text="Select an output folder",bg=self.frame2_background,fg=self.frame2_foreground)

    def resize(self):

        if self.geometry_method == 0:
            W = int(self.entryWidth_1.get())
            H = int(self.entryHeight_1.get())
        elif self.geometry_method == 1:
            W = int(self.entryWidth_2.get())
            H = int(W/2)                                                                             #CORREGGERE
        elif self.geometry_method == 2:
            H = int(self.entryHeight_3.get())
            W = int(H*2)                                                                             #CORREGGERE    
        else:
            print "%s - Errors in W, H"%(actual_time())

        if (self.oldW == 0 and self.oldH == 0):
            #print "%s - First cycle, ok. Are you ready?"%(actual_time())
            if (W>0 and H>0):
                self.ready_to_resize = True
                self.info_megapixel.config(text="%s\n%s\n%s Mpx"%(W,H,round(W*H*1.0/1000000,1)))
                self.logger.log("Ok, are you ready? ReClick to start resizing!")    
        elif (self.oldW != W or self.oldH != H) or (W==0 or H==0):
            self.ready_to_resize = False 
            self.info_megapixel.config(text="%s\n%s\n%s Mpx"%(W,H,round(W*H*1.0/1000000,1)))
            #print "%s - Something changed, you're not ready anymore"%(actual_time())
            self.logger.log("Something changed, you're not ready anymore")
            self.start_resizing.config(text="3. Resize!")
        elif self.ready_to_resize == True:
            #print "Resizing!", self.geometry_method, W, H
            self.logger.log("Resizing to %dx%s"%(W, H))
            self.batch_resizer(W,H)
        elif (W > 0 and H > 0):
            self.ready_to_resize = True
            self.info_megapixel.config(text="%s\n%s\n%s Mpx"%(W,H,round(W*H*1.0/1000000,1)))
            self.start_resizing.config(text="ReClick to confirm!")
            self.logger.log("ReClick to confirm and start resizing!")
        
        self.oldW = W
        self.oldH = H

    def batch_resizer(self,W,H):
        self.logger.log("Resizing (%s/%s) %s"%(0+1,len(self.image_list.namelist),self.image_list.namelist[0]))
        self.image_list.resize_a_single_image(0,W,H)

    def select_output_directory(self):
        self.image_list.set_destination_folder()
        df = self.image_list.destination_folder
        self.ready_to_set_resizer_switcher(df)
        
    def ready_to_set_resizer_switcher(self,folder):
        if type(folder) != str:
            if len(folder) > 20:
                points = "..."
            else:
                points = ""
            self.logger.log("Folder '%s' selected"%(points+self.image_list.destination_folder[-20:]))
            self.output_folder_text.config(text=folder[:28]+"...")    
            self.select_output_directory.config(text="Change folder",bg="#")
            self.select_images.config(text="Reset workflow")

            self.start_resizing.config(state="normal")
            self.frame_folder_selector.config(bg=self.excited_frame2_background)
            self.frame_number_2.config(bg=self.excited_frame2_background,fg=self.excited_frame2_foreground)
            self.output_folder_text.config(bg=self.excited_frame2_background,fg=self.excited_frame2_foreground)
            self.rb1.config(state="active")
            self.entryHeight_1.config(state="normal")
            self.entryWidth_1.config(state="normal")
            self.rb2.config(state="normal")
            self.rb3.config(state="normal")
        else:
            self.logger.log("Select an output folder")
            self.output_folder_text.config(text="Select an output folder")
            self.select_output_directory.config(text="Select output folder",bg="white")

            self.start_resizing.config(state="disabled")
            self.frame_folder_selector.config(bg=self.frame2_background)
            self.frame_number_2.config(bg=self.frame2_background,fg="#323232")
            self.output_folder_text.config(bg=self.frame2_background,fg="#ddd")
            self.rb1.config(state="disabled")
            self.rb2.config(state="disabled")
            self.rb3.config(state="disabled")
            self.entryHeight_1.config(state="disabled")
            self.entryWidth_1.config(state="disabled")
            self.entryWidth_2.config(state="disabled")
            self.entryHeight_3.config(state="disabled")

root = Tkinter.Tk()
app = App(root)

root.mainloop()
