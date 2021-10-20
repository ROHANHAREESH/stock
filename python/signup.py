from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image,ImageTk
from email_test import verification
import random
import re
import traceback
global n
def signup2(r):
    root2=Toplevel()
    root2.geometry('1000x720+250+50')
    root2.resizable(0,0)
    bgg=ImageTk.PhotoImage(file="images\stk2.jpg")
    myc1=Canvas(root2,width=1000,height=720,bd=0,highlightthickness=0)
    myc1.pack(fill='both',expand=True)
    myc1.create_image(0,0,image=bgg,anchor="nw")
    profile=ImageTk.PhotoImage(file="images\profile.png")
    myc1.create_image(452,100,image=profile,anchor="nw")
    btnim=ImageTk.PhotoImage(file="images\\back.png")
    myc1.create_text(420,20,text="Sign Up",anchor="nw",font="times 40 bold",fill="white")
    def do():
        root2.destroy()
        r.deiconify()
    btn=Button(myc1,image=btnim,bg="white",command=do)
    btn.place(x=50,y=250)
    
    name=Entry(myc1,font="times 20 ",fg="grey",width=20)
    name.place(x=360,y=230)
    em=Entry(myc1,font="times 20 ",fg="grey",width=20)
    em.place(x=360,y=300)
    otp=Entry(myc1,font="times 20 ",fg="grey",width=20)
    otp.place(x=360,y=400)
    pw=Entry(myc1,font="times 20 ",fg="grey",width=20)
    pw.place(x=360,y=470)
    rpw=Entry(myc1,font="times 20 ",fg="grey",width=20)
    rpw.place(x=360,y=540)
    name.insert(0,"Full Name")
    em.insert(0,"Email")
    otp.insert(0,"Enter OTP")
    pw.insert(0,"Create Password")
    rpw.insert(0,"re-enter Password")
    a=myc1.create_text(650,230,text="",anchor="nw",font="times 20 bold",fill="red")
    b=myc1.create_text(730,300,text="",anchor="nw",font="times 20 bold",fill="red")
    c=myc1.create_text(650,400,text="",anchor="nw",font="times 20 bold",fill="red")
    d=myc1.create_text(650,470,text="",anchor="nw",font="times 20 bold",fill="red")
    e1=myc1.create_text(650,540,text="",anchor="nw",font="times 20 bold",fill="red")
    def fname(e):
        myc1.itemconfigure(a,text="")
        if(name.get()=="Full Name"):
            name.delete(0,END)
            name.configure(fg="black")
    def email(e):
        myc1.itemconfigure(b,text="")
        if(em.get()=="Email"):
            em.delete(0,END)
            em.configure(fg="black")
    def onet(e):
        myc1.itemconfigure(c,text="")
        if(otp.get()=="Enter OTP"):
            otp.delete(0,END)
            otp.configure(fg="black")
    def pwd(e):
        myc1.itemconfigure(d,text="")
        if(pw.get()=="Create Password"):
            pw.delete(0,END)
            pw.configure(show="*",fg="black")
    def rpwd(e):
        myc1.itemconfigure(e1,text="")
        if(rpw.get()=="re-enter Password"):
            rpw.delete(0,END)
            rpw.configure(show="*",fg="black")
    name.bind("<Button-1>",fname)
    em.bind("<Button-1>",email)
    otp.bind("<Button-1>",onet)
    pw.bind("<Button-1>",pwd)
    rpw.bind("<Button-1>",rpwd)
    def everify():
        global n
        regex='^[A-Za-z]+[A-Za-z0-9_.-]*@gmail.com$'
        eid=em.get()
        if(re.match(regex,eid)):    
            n=str(random.randint(100000,999999))
            myc1.create_text(370,350,text="OTP SENT SUCCESSFULLY",anchor="nw",font="times 15 bold",fill="red")
            verification(em.get(),n)
        else:
            myc1.itemconfigure(b,text="enter valid email")
    def submit():
        rname='^[A-Za-z]+[A-Za-z\s]*'
        na=name.get()
        eq=em.get()
        ot=otp.get()
        pq=pw.get()
        rpq=rpw.get()
        flag=1
        if(re.match(rname,na)==None or na=="Full Name"):
            myc1.itemconfigure(a,text="enter valid name")
            flag=0
        if(ot=="" or ot=="Enter OTP"):
            myc1.itemconfigure(c,text="enter otp")
            flag=0
        if(pq=="" or pq=="Create Password"):
            myc1.itemconfigure(d,text="enter password")
            flag=0
        if(ot!="" and n!=ot):
            myc1.itemconfigure(c,text="wrong otp")
            flag=0
        if(pq!=rpq):
            myc1.itemconfigure(e1,text="match error")
            flag=0
        else:
            if(flag==1):
                uid=random.randint(1000000,9999999)
                try:
                    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="stocks")
                    con=mydb.cursor()
                    con.execute("insert into login(email,password) values(%s,%s)",(eq,pq))
                    con.execute("insert into shareholder(Full_name,uid,email) values(%s,%s,%s)",(na,uid,eq))
                    con.execute("insert into wallet(uid,w_amt,debit,credit,time) values(%s,0,0,0,0)",(uid,))
                    mydb.commit()
                    messagebox.showinfo("registration","Registration Successfull")
                    root2.destroy()
                    r.deiconify()
                except:
                    myc1.itemconfigure(b,text="Email already exists")
    signup=Button(myc1,text="Sign Up",bg="red",fg="White",height=0,width=7,font="times 17 bold",command=submit)
    signup.place(x=452,y=600)
    verify=Button(myc1,text="send otp",bg="blue",fg="White",height=0,width=7,font="times 12 bold",command=everify)
    verify.place(x=650,y=300)
    root2.mainloop()
