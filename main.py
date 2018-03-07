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

class image_list(): 

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

class App():

    def __init__(self,root):
        
        root.title("RESIZE")
        root.geometry("300x500")
        root.configure(background='#252525')
        root.iconbitmap("images/Iconv1.ico")

        self.hasImageList = False
        self.hasOutputFolder = False
        self.image_list = False
        self.output_folder = None

        self.ready_to_resize = False
        self.oldW,self.oldH = 0,0

    # HEADER ----------------------
        self.header = header(root,150,300,"images/Header1.png")

    # FRAME -----------------------
        self.frame1 = frame(root,"#151515","#1E824C","#CCC","#6EDFA4","#4DAF7C","#252525",None,10)
        self.number1 = frame_number(self.frame1,"1")

        self.frame2 = frame(root,"#202020","#319B5C","#CCC","#75EDAF","#58B283","#303030",None,10)
        self.number2 = frame_number(self.frame2,"2")

        self.frame3 = frame(root,"#242424","#42AD6E","#CCC","#6EDFA4","#6EB892","#343434",None,10)
        self.number3 = frame_number(self.frame3,"3")

        self.button_select_images = button(self.frame1,"Select images",self.select_images,"#ddd","black","#166139","#c3ffc3",0,1,6,18,0)
        self.button_select_folder = button(self.frame2,"Select output folder",self.select_folder,"#ddd","black","#166139","#c3ffc3",0,1,6,18,0)
        self.button_select_folder.is_clickable(False)
        # SET INNER TEXT EXAMPLE: self.button_select_images.set_inner_text("Click to Reset")

        self.text1 = frame_text(self.frame1,"Select some images")
        self.text2 = frame_text(self.frame2,"Select an output folder")

        self.subframe_frame3 = subframe(self.frame3,0,2,4,4,None)
        
        self.entry_selector_row1 = entry_selector(self.subframe_frame3.subframe,0,None,0,0,"W H","normal",8,3)
        self.entry_W_row1 = entry(self.subframe_frame3.subframe,"red","#202020","blue","orange","cyan",0,1,4)
        self.entry_H_row1 = entry(self.subframe_frame3.subframe,"red","#202020","blue","orange","cyan",0,2,4)

        self.entry_selector_row2 = entry_selector(self.subframe_frame3.subframe,1,None,1,0,"W","normal",8,3)
        self.entry_W_row2 = entry(self.subframe_frame3.subframe,"red","#202020","blue","orange","cyan",1,1,4)
        self.entry_H_row2 = entry(self.subframe_frame3.subframe,"red","#202020","blue","orange","cyan",1,2,4)

        self.entry_selector_row3 = entry_selector(self.subframe_frame3.subframe,2,None,2,0,"H","normal",8,3)
        self.entry_W_row3 = entry(self.subframe_frame3.subframe,"red","#202020","blue","orange","cyan",2,1,4)
        self.entry_H_row3 = entry(self.subframe_frame3.subframe,"red","#202020","blue","orange","cyan",2,2,4)

        root.config(bd=0)

    # MENU ------------------------
        self.menu = menu(root)

    # LOG
        self.logger = TraceConsole(root)
        self.logger.log("Welcome to RESIZƎ!")
        self.logger.log("Please select images to resize")

    # ROOT ------------------------
        
        #root.resizable(False, False)                ################################# LEVARE COMMENTO IN FUTURO

    # FRAME NUMBER 3 [GEOMETRIES AND RESIZE] ------
        self.geometry_method=0

        self.geometries_frame = Tkinter.Frame(root,bg="#303030",pady=10)
        self.geometries_frame.pack(fill="x")

        self.frame_number_3 = Tkinter.Label(self.geometries_frame,text="3",bg='#303030',fg="#404040", font=(selected_font, 30),padx=40)
        self.frame_number_3.grid(row=0,columnspan=2,column=0,rowspan=6)
      
        self.radioframe = Tkinter.Frame(self.geometries_frame,bg="#303030")
        self.radioframe.grid(row=0,columnspan=4,column=2,rowspan=4)

    # WH
        self.rb1 = Tkinter.Radiobutton(self.radioframe, text="W H",pady=3,font=(selected_font,9),\
            width=8,variable=self.geometry_method,value=0,state="disabled",command=self.enable_widget_1,indicatoron=0,bd=0,\
            background="#404040",activebackground="#F75C4C",selectcolor="#E74C3C")
        self.rb1.grid(row=0,column=0,pady=2) 

        self.entryWidth_1 = Tkinter.Entry(self.radioframe,width=7,bd=0,bg="#bbb",disabledbackground="#383838",disabledforeground="#505050",fg="#333",insertbackground="orange",state="disabled")
        self.entryWidth_1.grid(row=0,column=1,padx=2,ipady=4,sticky="e")
        self.entryHeight_1 = Tkinter.Entry(self.radioframe,width=7,bd=0,bg="#bbb",disabledbackground="#383838",disabledforeground="#505050",fg="#333",insertbackground="orange",state="disabled")
        self.entryHeight_1.grid(row=0,column=2,padx=2,ipady=4,sticky="w")

    # W
        self.rb2 = Tkinter.Radiobutton(self.radioframe,text="WIDTH",pady=3,font=(selected_font,9),\
            width=8,variable=self.geometry_method,value=1,state="disabled",command=self.enable_widget_2,indicatoron=0,bd=0,\
            background="#404040",activebackground="#F75C4C",selectcolor="#E74C3C")
        self.rb2.grid(row=1,column=0,pady=2)

        self.entryWidth_2 = Tkinter.Entry(self.radioframe,width=7,bd=0,\
            bg="#bbb",disabledbackground="#383838",disabledforeground="#505050",fg="#333",\
            insertbackground="orange",state="disabled")
        self.entryWidth_2.grid(row=1,column=1,padx=2,ipady=4,sticky="we")
    
    # H
        self.rb3 = Tkinter.Radiobutton(self.radioframe, text="HEIGHT",pady=3,font=(selected_font,9),\
            width=8,variable=self.geometry_method,value=2,state="disabled",command=self.enable_widget_3,indicatoron=0,bd=0,\
            background="#404040",activebackground="#F75C4C",selectcolor="#E74C3C")
        self.rb3.grid(row=2,column=0,pady=2)

        self.entryHeight_3 = Tkinter.Entry(self.radioframe,width=6,bd=0,bg="#bbb",disabledbackground="#383838",disabledforeground="#505050",fg="#333",insertbackground="orange",state="disabled")
        self.entryHeight_3.grid(row=2,column=1,padx=2,ipady=4,sticky="we")

    # [RESIZER] ------
        self.start_resizing = Tkinter.Button(self.geometries_frame,text="Resize!",command=self.resize,pady=6,state="disabled",width=17,bd=0)
        self.start_resizing.grid(row=5,column=2,ipadx=5,sticky=Tkinter.W)
    # END [RESIZER] ------

    # [MEGAPIXELS] -----

        self.info_megapixel= Tkinter.Label(self.radioframe,text="",font=(selected_font,8),width=9,anchor="w",bg="#303030",fg="#ddd")
        self.info_megapixel.grid(row=1,column=2,rowspan=2)

    # END [MEGAPIXELS] -----

    # END FRAME NUMBER 3 [GEOMETRIES AND RESIZE] ------ 



    def enable_widget_1(self):
        self.logger.log("Enter output Width and Height")
        self.entryWidth_1.config(state="normal")
        self.entryHeight_1.config(state="normal")
        self.entryWidth_2.config(state="disable")
        self.entryHeight_3.config(state="disable")
        self.geometry_method=0

    def enable_widget_2(self):
        self.logger.log("Enter output Width")
        self.rb1.config(state="normal")
        self.entryWidth_1.config(state="disable")
        self.entryHeight_1.config(state="disable")
        self.entryWidth_2.config(state="normal")
        self.entryHeight_3.config(state="disable")
        self.geometry_method=1

    def enable_widget_3(self):
        self.logger.log("Enter output Height")
        self.rb1.config(state="normal")
        self.entryWidth_1.config(state="disable")
        self.entryHeight_1.config(state="disable")
        self.entryWidth_2.config(state="disable")
        self.entryHeight_3.config(state="normal")
        self.geometry_method=2

    def frame2_excited(self):
        self.button_select_images.set_inner_text("Reset workflow")
        self.button_select_folder.set_inner_text("Reset folder")
        self.button_select_folder.excited()
        self.frame2.excited()
        self.number2.excited()
        self.text2.excited()

    def frame2_unexcited(self):
        self.button_select_folder.set_inner_text("Select output folder")
        self.output_folder = None
        self.button_select_folder.unexcited()
        self.frame2.unexcited()
        self.number2.unexcited()
        self.text2.unexcited()

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

    def select_images(self):
        if self.image_list == False:
            self.image_list = image_list()
            if self.image_list.listIsEmpty == True:
                self.image_list = False
            elif self.image_list.listIsEmpty == False:
                self.frame1_excited(len(self.image_list.namelist))
        else:
            self.frame1_unexcited()

    def select_folder(self):
        # Se l'output folder non è ancora settata prova a settarla
        if self.output_folder == None:
            # Chiamo il metodo per popolare la variabile
            self.image_list.set_destination_folder()
            self.output_folder = self.image_list.destination_folder
            self.frame2_excited()
        # Altrimenti lasciala non settata
        else:            
            self.frame2_unexcited()

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