from tkinter import *
from tkinter import messagebox as mb
import sqlite3 as sq

def stu_database():
   con=sq.connect('studentmanage.db')
   cur=con.cursor()
   name=e1.get()
   rollno=e2.get()
   age=e3.get()
   gender=var.get()
   email=e4.get()
   p=en1.get()
   c=en2.get()
   m=en3.get()
   tot=int(en1.get())+int(en2.get())+int(en3.get())
   cur.execute('CREATE TABLE IF NOT EXISTS studentdata (Name TEXT,rollno TEXT,age TEXT,gender TEXT,email TEXT,physics TEXT,chemistry TEXT,math TEXT,total TEXT)')
   cur.execute('INSERT INTO studentdata(Name,rollno,age,gender,email,physics,chemistry,math,total) values(?,?,?,?,?,?,?,?,?)',(name,rollno,age,gender,email,p,c,m,tot))
   con.commit()
   con.close()
   e1.delete(0,END)
   e2.delete(0,END)
   e3.delete(0,END)
   e4.delete(0,END)
   en1.delete(0,END)
   en2.delete(0,END) 
   en3.delete(0,END)
 
def read_stu_data():
   con=sq.connect('studentmanage.db')
   cur=con.cursor()
   cur.execute('SELECT * FROM studentdata')
   data=cur.fetchall()
   m=1
   for i in data:
       print(f"{m}.")
       print(f"name->{i[0]}")
       print(f"age-->{i[2]}")
       print(f"Roll no-->{i[1]}")
       print(f"Gender-->{i[3]}")
       print(f"email-->{i[4]}")
       print(f"physics-->{i[5]}")
       print(f"CHemistry-->{i[6]}")
       print(f"math-->{i[7]}")
       print(f"TOTAL-->{i[8]}")
       print("________________")
       m+=1

def search_stu():
    con=sq.connect('studentmanage.db')
    cur=con.cursor()
    cur.execute("SELECT * FROM studentdata")
    data=cur.fetchall()
    m=1
    for i in data:
              if entrystu.get()==i[0]:
                       print(f"{m}.")
                       print(f"name->{i[0]}")
                       print(f"age-->{i[2]}")
                       print(f"Roll no-->{i[1]}")
                       print(f"Gender-->{i[3]}")
                       print(f"email-->{i[4]}")
                       print(f"physics-->{i[5]}")
                       print(f"CHemistry-->{i[6]}")
                       print(f"math-->{i[7]}")
                       print(f"TOTAL-->{i[8]}")
                       print("________________")
                       break
#m+=1
                        

def add_stu_data():
  screen=Toplevel(root)
  screen.geometry("500x570")
  screen.resizable(0,0)
  screen.title("Student registration")
  global e1,e2,e3,var,e4
  Label(screen,text="student Profile",font=("arial",25),fg="red").pack()
 
  label=Label(screen,text="STudent Name:-",font=("arial",15),fg="yellow",bg="blue").place(x=40,y=60)
  e1=Entry(screen,width=25,font=("calibri",15))
  e1.place(x=230,y=65)

  Label(screen,text="STudent RollNO:-",font=("arial",15),fg="yellow",bg="blue").place(x=40,y=120)
  e2=Entry(screen,width=25,font=("calibri",15))
  e2.place(x=230,y=130)

  Label(screen,text="STudent Age:-",font=("arial",15),fg="yellow",bg="blue").place(x=40,y=180)
  e3=Entry(screen,width=25,font=("calibri",15))
  e3.place(x=230,y=190)

  Label(screen,text="GENDER:-",font=("arial",15),fg="yellow",bg="blue").place(x=40,y=240)
  var=StringVar()

  Radiobutton(screen,text="MALE",variable=var,value='male',font=("arial",15),fg="red").place(x=210,y=240)
  Radiobutton(screen,text="FEMALE",variable=var,value='female',font=("arial",15),fg="red").place(x=300,y=240)

  Label(screen,text="EMAIL:-",font=("arial",15),fg="yellow",bg="blue").place(x=40,y=300)
  e4=Entry(screen,width=25,font=("calibri",15))
  e4.place(x=230,y=305)

  Label(screen,text="MARKS IN PCM:-",font=("arial",15),fg="yellow",bg="blue").place(x=40,y=350)
  Label(screen,text="PHYSICS:-",font=("arial",15),fg="yellow",bg="blue").place(x=40,y=400)
  global en1
  en1=Entry(screen,width=6,font=("calibri",15))
  en1.place(x=110,y=400)

  Label(screen,text="CHEMISTRY:-",font=("arial",15),fg="yellow",bg="blue").place(x=180,y=400)
  global en2
  en2=Entry(screen,width=6,font=("calibri",15))
  en2.place(x=275,y=400)

  Label(screen,text="MATH:-",font=("arial",15),fg="yellow",bg="blue").place(x=345,y=400)
  global en3
  en3=Entry(screen,width=6,font=("calibri",15))
  en3.place(x=400,y=400)
  global x,en4
  def total_no():
         x=IntVar()
         en4=Entry(screen,width=20,font=("calibri",15),textvariable=x)
         en4.place(x=90,y=430)
         t=str(int(en1.get())+int(en2.get())+int(en3.get()))+" out of 300"
         x.set(t)
  Button(screen,text="TOTAL",font=("calibri",15),bg="yellow",fg="blue",command=total_no).place(x=40,y=430)
  Button(screen,text="DATA",font=("calibri",15),bg="yellow",fg="blue",command=stu_database).place(x=100,y=470)

def search_stu_data():
                     screen2=Toplevel(root)
                     screen2.geometry("400x230")
                     screen2.resizable(0,0)
                     screen2.title("SEARCHING")
                     Label(screen2,text="Search Student:",font=("arial",15),fg="yellow",bg="blue").pack()
                     Label(screen2,text="ENTER NAME To search",font=("arial",15),fg="yellow",bg="blue").place(x=90,y=80)
                     global entrystu
                     entrystu=Entry(screen2,width=25,font=("calibri",13))
                     entrystu.place(x=75,y=120)
                     Button(screen2,text="SEARCH",font=("calibri",15),bg="yellow",fg="blue",command=search_stu).place(x=75,y=180)



root=Tk()
root.geometry("500x400")
root.title("SCHOOL MANAGEMENT")


label=Label(root,text="SCHOOL MANAGEMENT SYSTEM",font=("arial",25),bg="blue",fg="yellow")
label.pack()

Button(root,text='ADD STUDENT DATA',font=("arial",15),command=add_stu_data).place(x=60,y=60)
Button(root,text="SEARCH STUDENT DATA",font=("arial",15),command=search_stu_data).place(x=40,y=120)
Button(root,text="SHOW STUDENT DATA",font=("arial",15),command=read_stu_data).place(x=40,y=180)

root.mainloop()
