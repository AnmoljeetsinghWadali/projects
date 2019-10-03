from tkinter import *
from tkinter.ttk import Combobox as cb
from tkinter import messagebox
import http.client
import json
#import pyfiglet as pf
import sqlite3 as s
import time as t
import pyautogui as py
def sms(a):   
 conn = http.client.HTTPConnection("api.msg91.com")
 payload ='''{
  "sender": "wadali",
  "route": "4",
  "country": "91",
  "sms": [
    {
      "message":"anmol",
      "to": [
        "9888997293"  
      ]
    }   
  ]
 }'''
 x=eval(payload)
 x['sms'][0]['message']=a
 y=json.dumps(x)
 print(y)
 headers = {
    'authkey': "272220AmMtDTtmK5cb186a9",
    'content-type': "application/json"}
 print(payload)
 conn.request("POST", "/api/v2/sendsms?country=91&sender=&route=&mobiles=&authkey=&encrypt=&message=&flash=&unicode=&schtime=&afterminutes=&response=&campaign=",y, headers)
 res = conn.getresponse()
 data = res.read()
 print(data.decode("utf-8"))



def database(a,b,c,d,e):
    conn=s.connect('wadali.db')
    time=t.asctime()
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS jeweller1(date TEXT,item TEXT,purity TEXT,rate TEXT,weight  TEXT,netamount  TEXT)')
    cursor.execute('INSERT INTO jeweller1(date,item,purity,rate,weight,netamount)VALUES(?,?,?,?,?,?)',(time,a,b,c,d,e))
    conn.commit()
    print('data added')
    
def showdata():
    a=py.password(text='ENTER THE PASSWORD TO ACCESS THE DATA BASE',title='ACCESS',default='',mask='*',root=root)
    print(a)
    if a=='anmol':
       conn=s.connect('wadali.db')
       cur=conn.cursor()
       cur.execute('SELECT * FROM jeweller1')
       ans=cur.fetchall()
       #print(type(ans[0]))
       for i in ans:
          print(i)
       p=messagebox.showinfo('DATA',str(ans))
       top=Toplevel(root)
       top.config(background='grey')
       top.geometry('600x600+800+300')
       top.resizable(width=False,height=False)
       top.title('BILLING SYSTEM')
       search=Label(top,text='SEARCH BY ',bg='green',fg='orange',font=('bold',15))
       search.place(x=50,y=50)
    
       l1=['DATE','NAME']
       combo=cb(top,value=l1,width=30)
       combo.set('SELECT TYPE')
       combo.place(x=250,y=50)

       enter=Label(top,text='ENTER THE NAME/DATE:- ',bg='green',fg='orange',font=('bold',15))
       enter.place(x=50,y=100)

       enter1=Entry(top,width=30)
       enter1.place(x=250,y=100)
    else:
        messagebox.showerror('FAILURE','SORRY PERMISSION TO  ACCESS DATABASE IS DENIED')
        exit()
    
    
    
    
        
    
    
def total():
    if c2.get()!='' and c1.get()!='' and e3.get()!='' and w.get()!='':
   
    
       print(c1.get()) #item name
       print(c2.get())  # purity
       print(e3.get())  # rate
       print(w.get())  # weight
       print(pol.get()) # POLISH
       print(l.get())#labour
       netweight=float(w.get())+float(pol.get())
       print(netweight)
       y=float(l.get())+float(e3.get())
       amount=int(netweight*y)
       
       print(amount)
       tax=amount*0.03
       tax=round(tax,2)
       
       a='ITEM NAME-'+c1.get()+'\n PURITY-'+c2.get()+'\n NET WEIGHT-'+str(netweight)+' grams\nRATE (per gm)-'+e3.get()+' \n\nAMOUNT -'+str(amount)+' Rupees\nSGST @1.5% -'+str(round(tax/2,2))+' Rupees\nCGST @1.5% -'+str(round(tax/2,2))+' Rupees\nNET BALANCE--'+str(int(amount+tax))+' Rupees'
       p=messagebox.showinfo('BALANCE',a)
       try:
           sms(a)
       except:
          print("SMS NOT SENT")


          
       a=c1.get()
       b=c2.get()
       c=e3.get()
       d=w.get()
       e=str(int(amount+tax))
       database(a,b,c,d,e) # adding data to database

       
       c1.delete(0,END)
       c2.delete(0,END)
       e3.delete(0,END)
       w.delete(0,END)
       pol.delete(0,END)
       l.delete(0,END)
       c2.set('SELECT ITEM')
       c1.set('SELECT PURITY')
    
    

root=Tk()
root.config(background='grey')
root.geometry('600x600+800+300')
root.resizable(width=False,height=False)
root.title('BILLING SYSTEM')
#f=pf.figlet_format(text='JEWELLERY',font='digital')
label=Label(root,text='JEWELLERY',bg='BLACK',fg='white',font=('',60))
label.pack()

label1=Label(root,text='ITEM',bg='green',fg='orange')
label1.place(x=65,y=210)

l=['RING','TOPS','WALI','KARA','ANY OTHER STUFF']
c1=cb(root,value=l,width=25)
c1.set('SELECT ITEM')
c1.place(x=250,y=210)

label2=Label(root,text='PURITY & TYPE',bg='green',fg='orange')
label2.place(x=65,y=250)

l1=['916 HALLMARK','750 HALLMARK','ANY OTHER']

c2=cb(root,value=l1,width=25)
c2.set('SELECT PURITY')
c2.place(x=250,y=250)

label3=Label(root,text='RATE (per gram)',bg='green',fg='orange')
label3.place(x=65,y=290)

e3=Entry(root,width=25)
e3.place(x=250,y=290)

weight=Label(root,text='WEIGHT OF ITEM (In Grams)',bg='green',fg='orange')
weight.place(x=65,y=330)

w=Entry(root,width=25)
w.place(x=250,y=330)

polish=Label(root,text='POLISH(IN Grams)',bg='green',fg='orange')
polish.place(x=65,y=370)

pol=Entry(root,width=25)
pol.place(x=250,y=370)

labour=Label(root,text='LABOUR (PER Grams)',bg='green',fg='orange')
labour.place(x=65,y=410)

l=Entry(root,width=25)
l.place(x=250,y=410)

button=Button(root,text='TOTAL',width=20,bg='green',fg='orange',command=total)
button.place(x=250,y=460)

b=Button(root,text='SHOW DATA STORED',width=20,bg='green',fg='orange',command=showdata)
b.place(x=250,y=490)

root.mainloop()
