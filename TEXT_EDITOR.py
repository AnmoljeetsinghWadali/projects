#EDITOR project  
from tkinter import *
from tkinter import filedialog
class texteditor:
    currentfile="nofile"
    def openfile(self):
        print('OPening file')
        open_return=filedialog.askopenfile(initialdir="/",title="select file to open",filetypes= (("Python file",(".py",".pyw")),("text files","*.txt"),("all files","*.*")))
        if open_return !=None:
          self.text_area.delete(1.0,END)
          for line in open_return:
             self.text_area.insert(END,line)
          self.currentfile=open_return.name
        open_return.close()
        
        
    def saveasfile(self):
        f=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
        if f is None:
            return
        text2save=self.text_area.get(1.0,END)
        self.currentfile=f.name
        f.write(text2save)
        f.close()
        
    def savefile(self):
        if self.currentfile=="nofile":
           self.saveasfile()
        else:
             f=open(self.currentfile,'w+')
             f.write(self.text_area.get(1.0,END))
             f.close() 
    def newfile(self):
        self.text_area.delete(1.0,END)
        self.currentfile='nofile'
        
    def copytext(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())
    def cuttext(self):
        self.copytext()
        self.text_area.delete("sel.first","sel.last")
    def pastetext(self):
        self.text_area.insert(INSERT,self.text_area.clipboard_get())
     
    def __init__(self,master):
        self.master=master
        master.title("ANMOL  NOTEPAD")
        self.text_area=Text()
        self.text_area.pack(fill=BOTH,expand=1)
        self.mainmenu=Menu()
        self.master.config(menu=self.mainmenu)
        # creating file menu 
        self.filemenu=Menu(self.mainmenu)
        self.filemenu.add_command(label='OPEN',command=self.openfile)
        self.filemenu.add_separator()
        self.mainmenu.add_cascade(label='FILE',menu=self.filemenu)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='NEW',command=self.newfile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='SAVE AS',command=self.saveasfile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='SAVE',command=self.savefile) 
        self.filemenu.add_separator()
        self.filemenu.add_command(label='EXIT',command=self.master.destroy)
        
        # creating Editc menu 
        self.editmenu=Menu(self.mainmenu)
        self.mainmenu.add_cascade(label='EDIT',menu=self.editmenu) 
        self.editmenu.add_command(label="COPY",command=self.copytext)
        self.editmenu.add_command(label="CUT",command=self.cuttext)
        self.editmenu.add_command(label="PASTE",command=self.pastetext)
root=Tk()
te=texteditor(root)
root.mainloop()
