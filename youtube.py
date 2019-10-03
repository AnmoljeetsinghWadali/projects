import tkinter as tk
from tkinter import *
from pytube import YouTube as yt
from tkinter import messagebox ,filedialog 

def createwidgets():
   link=Label(root,text="ENTER THE VIDEO LINK",bg="skyblue")
   link.grid(row=1,column=0)

   root.linktext=Entry(root,width=60)
   root.linktext.grid(row=1,column=1,columnspan=2)

   dlabel=Label(root,text="save",bg="skyblue")
   dlabel.grid(row=2,column=0)

   root.dtext=Entry(root,width=30)
   root.dtext.grid(row=2,column=1)
   
   bb=Button(root,text="BROWSE",command=browse,width=15)
   bb.grid(row=2,column=2)
   
   dbutton=Button(root,text="DOWNLOAD",command=download,width=15)
   dbutton.grid(row=3,column=1)
def browse():
  root.dir=filedialog.askdirectory(initialdir="/Users/harsimranwadali/Desktop/gui_projects")
  root.dtext.insert('1',root.dir)

def download():
  getvideo=yt(root.linktext.get())
  videostream=getvideo.streams.first()
  videostream.download(root.dir)
  messagebox.showinfo("SUCCESS","saved in"+root.dir)

root=tk.Tk()
root.geometry("530x110")
root.title("HELLO")
#root.resizable(False,False)
root.config(background="skyblue")
createwidgets()
root.mainloop()
