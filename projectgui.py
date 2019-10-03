from tkinter import *
from tkinter.ttk import Combobox as cb
from sqlwithgui import *
def cal(days,roomtype):
  
    roomtype=roomtype.lower()
    if roomtype=='normal':
        total=int(days)*1500
    elif roomtype=='king':
        total=int(days)*5000
    elif roomtype=='deluxe': 
        total=int(days)*3000
    elif roomtype=='honeymoon':
        total=int(days)*10000
    return total

    
def addinfo():
    name=l1.get()
    print(name)
    address=l2.get()
    print(address)
    phoneno=l3.get()
    print(phoneno)
    days=l4.get()
    print(days)
    roomtype=c1.get()
    print(roomtype)
    t=l5.get()
    insert(name,address,phoneno,days,roomtype,t)

window=Tk() 
#window.geometry('800x400')
window.title('HOTEL MANAGEMENT SYSTEM')
window.config(background='grey')
label1=Label(window,text='NAME',bg='BLACK',fg='white')
label1.grid(row=4,column=4)
l1=Entry(window,width=25)
l1.grid(row=4,column=6)

label2=Label(window,text='ADDRESS',bg='BLACK',fg='white')
label2.grid(row=8,column=4)
l2=Entry(window,width=25)
l2.grid(row=8,column=6)

label3=Label(window,text='PHONE NO',bg='BLACK',fg='white')
label3.grid(row=12,column=4)
l3=Entry(window,width=25)
l3.grid(row=12,column=6)


label4=Label(window,text='No OF DAYS',bg='BLACK',fg='white')
label4.grid(row=16,column=4)
l4=Entry(window,width=25)
l4.grid(row=16,column=6)

label5=Label(window,text='ROOM TYPE',bg='BLACK',fg='white')
label5.grid(row=20,column=4)
l=['KING','1 BHK','DELUX','HONEYMOON','ANY OTHER TYPE']
c1=cb(window,value=l,width=25)
c1.set('SELECT ROOM TYPE')
c1.grid(row=20,column=6)
q=StringVar()
label6=Label(window,text='AMOUNT ',bg='BLACK',fg='white')
label6.grid(row=24,column=4)
l5=Entry(window,textvariable=q,width=25)
l5.grid(row=24,column=6)
amount=Button(window,text='CALCULATE',width=20,bg='green',fg='orange')
amount.grid(row=24,column=8)
 
b1=Button(window,text='VIEW ALL',width=20,bg='green',fg='orange',command=view)
b1.grid(row=30,column=4)

b2=Button(window,text='ADD ENTRY',width=20,bg='green',fg='orange',command=addinfo)
b2.grid(row=34,column=4)

b3=Button(window,text='DELETE SELECTED',width=20,bg='green',fg='orange')
b3.grid(row=38,column=4)

b4=Button(window,text='SEARCH ENTRY',width=20,bg='green',fg='orange')
b4.grid(row=30,column=6)
 
b5=Button(window,text='UPDATE SELECTED',width=20,bg='green',fg='orange')
b5.grid(row=34,column=6)



listbox=Listbox(window,height=20,width=59)
listbox.grid(row=40,column=6  ,rowspan=6,columnspan=2)


s=Scrollbar(window,)
s.grid(row=40,column=5,sticky='ns',rowspan=4 )

listbox.configure(yscrollcommand=s.set)
s.configure(command=listbox.yview)


window.mainloop()  
