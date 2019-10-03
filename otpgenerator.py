import random
import  smtplib
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import re


def createwidgets():
    emaillabel=Label(root,text="Enter your email id-",bg='grey')
    emaillabel.grid(row=0,column=1,padx=5,pady=5)

    root.emailentry=Entry(root,textvariable=emailid,width=30)
    root.emailentry.grid(row=0,column=2,padx=5,pady=5)

    sendotpbutton=Button(root,text='send otp',command=sendotp,width=20)
    sendotpbutton.grid(row=0,column=3,padx=5,pady=5)

    otplabel=Label(root,text="Enter your otp-",bg='grey')
    otplabel.grid(row=1,column=1,padx=5,pady=5)


    root.otpentry=Entry(root,textvariable=otp,width=30)
    root.otpentry.grid(row=1,column=2,padx=5,pady=5)

    validotpbutton=Button(root,text='validate otp',command=validotp,width=20)
    validotpbutton.grid(row=1,column=3)    

def mail(sub,msg):
    eid=""
    pwd=""
    try:
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(eid,pwd)
        message="subject:{}\n\n{}".format(sub,msg)
        server.sendmail(eid,eid,message)
        server.quit()
        print("SUCCESSFULLY SENT")
    except:
        print("email failed")
def check(email):
    regex="^\w+([\.-]?\w+)*@\w+([\.-]?\w)*(\.\w{2,3})+$"
    if re.search(regex,email):
        print("VALID EMAIL")
        return 1
        
    else:
        messagebox.showerror("ERROR","EMAIL  INVALID")
        print("INVALID EMAIL")
        return None
        
def sendotp():
    
    useremail=emailid.get()
    a=check(useremail)
    if(a==1):
            nos='0123456789'
            root.genotp=''
    
            for i in range(6):
                     root.genotp+=nos[int(random.random()*10)]
            
            msg='your otp is '+root.genotp   
            sub="OTP VALIDATION"
            mail(sub,msg)
            otpsendlabel=Label(root,text="OTP SENT TO "+useremail,bg='grey')
            otpsendlabel.grid(row=2,column=1,padx=5,pady=5,columnspan=3)

def validotp():
   userotp=otp.get()
   systemotp=root.genotp
   regex=r'\d{6}'
   a=re.search(regex,userotp)
   if a !=None:
       if userotp==systemotp:
          messagebox.showinfo("SUCCESS","OTP VALIADTED")
          root.otpentry.delete('0','end')
          root.emailentry.delete('0','end')
       else:
          messagebox.showerror("ERROR","OTP INVALID")
          root.otpentry.delete('0','end')
          root.emailentry.delete('0','end')
   else:
        messagebox.showerror("ERROR","PLZZ ENTER THE 6 DIGITS OTP")
        root.otpentry.delete('0','end')
    

root=tk.Tk()
root.title('emailotp')
root.resizable(True,True)
root.config(background='grey')

emailid=StringVar()
otp=StringVar()

createwidgets()

root.mainloop()
