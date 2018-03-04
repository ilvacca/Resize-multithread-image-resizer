import Tkinter
from supports import *

selected_font = "Helvetica"

class TraceConsole:
    
    def __init__(self,root):
                
        # Container dei widget "Text" e "Scrollbar"
        self.logger_container = Tkinter.Frame()
        self.logger_container.pack()

        # Widget "Text"
        self._log = Tkinter.Text(self.logger_container, wrap=Tkinter.NONE, height=4,font=(selected_font, 8))
        self._log.configure(fg="#bbbbbb", bg="#404040",bd=0,padx=8,pady=8)
        #self._log.grid(row=0,column=0,columnspan=10)
        self._log.pack(fill="x")
        
        # Widget "Scrollbar"
        #self._scrollb = Tkinter.Scrollbar(self.logger_container, orient=Tkinter.VERTICAL,bg="red",activebackground="blue",bd=0)
        #self._scrollb.configure(command=self._log.yview)
        #self._scrollb.grid(row=0,column=10,columnspan=1,sticky="nes")
        
        #self._log.config(yscrollcommand=self._scrollb.set)

    def log(self, msg, level=None):
        # La funzione della classe "TraceConsole" che scrive nel log
        self._log.insert('end',actual_time()+" - "+msg+"\n")
        self._log.see(Tkinter.END)