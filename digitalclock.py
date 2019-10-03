import tkinter as tk
from tkinter import *
from time import strftime as st

def createwidgets():
   root.date=Label(root,text="DATE:- "+st("%d/%m/%Y"),font=("Helvetica",50),bg="skyblue",fg="white")
   root.date.grid(sticky='nw')
   root.time=Label(root,font=("Helvetica",100),bg="skyblue",fg="white")
   root.time.grid(sticky='nw')
   
   update()
def update():
    root.time.config(text=st("%H:%M:%S"))
    root.time.after(1000,update)
    

root=Tk()
root.title("DIGITAL CLOCK")
root.config(bg='skyblue')
#root.geometry("500x300")
root.resizable(False,False)
createwidgets()
root.mainloop()
