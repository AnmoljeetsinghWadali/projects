from tkinter import *
def b1():
    print("BUTTON1 IS PRESSED")
def b2():
    print("BUTTON2 IS PRESSED")
def b3():
    print("BUTTON3 IS PRESSED")
def b4():
    print("BUTTON4 IS PRESSED")

root =Tk()
root.title("GUI")
label=Label(root,text="PRESS THE BUTTON")
label.pack()
frame=Frame(root,width=100,height=100)
button1=Button(frame,text='B1',command=b1)
button2=Button(frame,text='B2',command=b2)
button3=Button(frame,text='B3',command=b3)
button4=Button(frame,text='B4',command=b4)
button1.pack(side=LEFT)   # LEFT,RIGHT,TOP,BOTTOM
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
frame.pack()

frame2=Frame(root)
button5=Button(frame2,text='hello')
button5.pack()
frame2.pack()

root.mainloop()
print("bye") #printed only when the cancel is pressed

