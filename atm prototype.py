import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from tkinter import *
from tkinter import messagebox
import pyautogui as p
import cv2
pin='1234'
bal=10000
i=0

def captureimage():
 try:
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    imagename='anmol12'+'.png'
    cv2.imwrite(imagename, image)
    del(camera)
    
    email_user = ''
    email_password = ''
    email_send = ''
    subject = 'subject'
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject
    body = 'Hi there,Somebody is trying to login to Bank Account!'
    msg.attach(MIMEText(body,'plain'))
    attachment  =open(imagename,'rb')
    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+imagename)
    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)
    server.sendmail(email_user,email_send,text)
    server.quit()
 except:
      print("EMAIL NOT SENT")
      

def mail(msg):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("anmolwadali1998@gmail.com", "anmolwadali41")
        server.sendmail("anmolwadali1998@gmail.com", "anmolwadali1998@gmail.com", msg)
        server.quit()
def check():
    p.confirm(text='YOU CURRENT BALANCE IS '+str(bal),title='BALANCE STATUS',buttons=['OKAY'])
def withdraw():
    global bal
    amount=p.prompt(text='ENTER AMOUNT TO WITHDRAW',title='WITHDRAW STATUS',default='')
    if not(amount == None):
       bal=bal-int(amount)
       msg="You have withdrawn -"+(amount)+"rupees."+"\nYour current balance is "+str(bal)
       #mail(msg)

       
def changepin():
    global pin
    newpin=p.password(text='ENTER NEW PIN',title='CHANGE PIN',default='',mask='*')
    if newpin:
        pin=newpin
        p.confirm(text='YOUR  PIN HAS BEEN CHANGED SUCCESSFULLY',title='CONFIRMATION',buttons=['OKAY'])
        msg="YOUR PIN HAS BEEN CHANGED SUCCESSFULLY"
        #mail(msg)
        
    
def login():
    print("successfully login")
    a=p.password(text='enter pin',title='PIN LOGIN',default='',mask='*')
    print(a)
    global pin
    global bal
    if a==pin:
        top=Toplevel()
        top.geometry('500x300+300+200')
        label=Label(top,text='PRESS THE OPTION',bg='red')
        label.pack(fill=X)
        frame=Frame(top,width=100,height=100)
        b1=Button(frame,text='CHECK BALANCE',command=check)
        b2=Button(frame,text='WITHDRAW',command=withdraw)
        b3=Button(frame,text='CHANGE PIN',command=changepin)
        b4=Button(frame,text='EXIT',command=top.destroy)
        b1.pack()
        b2.pack()
        b3.pack()
        b4.pack()
        frame.pack()
        
        
    else:
       global i
       answer= messagebox.askretrycancel('WRONG PIN','TRY AGAIN')
       i=i+1
       print(answer) 
       if answer==True and i<3:
           login()
       elif i>=3:
            p.confirm(text='SORRY YOU HAVE REACHED LOGIN LIMIT',title='LOGIN LIMIT',buttons=['OKAY'])
            captureimage()
            root.destroy()
            
           

root=Tk()
root.title('ATM PROTOTYPE')
root.geometry('500x300+300+200')
label=Label(root,text='WELCOME TO ATM PROTOTYPE',bg='red',fg='green')
#label.pack(fill=X)
label.grid(columnspan=4)

name=Label(root,text='NAME',bg='green')
pas=Label(root,text='PASSWORD',bg='green')
entry1=Entry(root)
entry2=Entry(root)
name.grid(row=1,column=0,sticky=E)
entry1.grid(row=1,column=1)
pas.grid(row=2,column=0)
entry2.grid(row=2,column=1)
Login=Button(root,text='LOGIN',command=login)
Login.grid(columnspan=3)
root.mainloop()
print("BYE BYE ")
