import Tkinter
from supports import *

class TraceConsole:
    
    def __init__(self,root):

        # Color properties
        self.bg = "#333"
        self.fg = "#999"
        self.font = ("Arial",8)

        self.padding = 6
        self.bd = 0

        # Container dei widget "Text" e "Scrollbar"
        self.logger_container = Tkinter.Frame()
        self.logger_container.pack()

        # Instancer
        self._log = Tkinter.Text(self.logger_container, wrap=Tkinter.NONE, height=4,font=self.font)
        self._log.configure(fg=self.fg,bg=self.bg,bd=self.bd,padx=self.padding,pady=self.padding)
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