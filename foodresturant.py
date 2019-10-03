from tkinter import *
from tkinter.ttk import Combobox as cb
from tkinter import messagebox
def total():
    if c2.get()!='' and c1.get()!='' and e3.get()!='':
     print(c2.get())
     print(e3.get())
     p=int(c2.get())*int(e3.get())
     t=(p*5)/100
     total=p+t
     amount='ITEM NAME-'+c1.get()+'\n Quantity-'+c2.get()+'\nNET AMOUNT --'+str(total)
     p=messagebox.showinfo('BALANCE',amount)
     c1.delete(0,END)
     c2.delete(0,END)
     e3.delete(0,END)
     c2.set('SELECT QUANTITY')
     c1.set('SELECT THE FOOD ITEM')
    
def additem():
    print('item added')

root=Tk()
root.geometry('500x500')
root.title('bill system')
label=Label(root,text='food resturant')
label.pack()

label1=Label(root,text='food item')
label1.place(x=65,y=110)

l=['a','b','c','d','e']
c1=cb(root,value=l,width=25)
c1.place(x=250,y=120)

label2=Label(root,text='Quantity')
label2.place(x=65,y=165)

l1=list(range(1,101))

c2=cb(root,value=l1,width=25)
c2.set('select quantity')
c2.place(x=250,y=170)

label3=Label(root,text='price')
label3.place(x=65,y=220)

e3=Entry(root,width=25)
e3.place(x=250,y=230)

button=Button(root,text='total',width=20,command=total)
button.place(x=130,y=280)

b=Button(root,text='SELECT',width=20,command=additem)
b.place(x=130,y=300)

root.mainloop()
