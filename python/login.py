from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from signup import signup2
from lostocks import stock
import mysql.connector
import traceback
import re
def log(r):
    root1=Toplevel()
    root1.geometry('1000x720+250+50')
    root1.resizable(0,0)
    bgg=ImageTk.PhotoImage(file="images\stk2.jpg")
    myc1=Canvas(root1,width=1000,height=720,bd=0,highlightthickness=0)
    myc1.pack(fill='both',expand=True)
    myc1.create_image(0,0,image=bgg,anchor="nw")
    profile=ImageTk.PhotoImage(file="images\profile.png")
    myc1.create_image(452,130,image=profile,anchor="nw")
    btnim=ImageTk.PhotoImage(file="images\\back.png")
    myc1.create_text(420,20,text="Sign In",anchor="nw",font="times 40 bold",fill="white")
    def do():
        root1.destroy()
        r.deiconify()
    btn=Button(myc1,image=btnim,bg="white",command=do)
    btn.place(x=50,y=250)
    em=Entry(myc1,font="times 20 ",fg="grey",width=20)
    em.place(x=360,y=280)
    pw=Entry(myc1,font="times 20 ",fg="grey",width=20)
    pw.place(x=360,y=360)
    em.insert(0,"Email")
    pw.insert(0,"Password")
    a=myc1.create_text(650,280,text="",anchor="nw",font="times 22 bold",fill="red")
    b=myc1.create_text(650,360,text="",anchor="nw",font="times 22 bold",fill="red")
    def signin1():
        regex='^[A-Za-z]+[A-Za-z0-9_.-]*@gmail.com$'
        eid=em.get()
        p=pw.get()
        if(re.match(regex,eid)):
            if(p=="Password" or p==""):
                myc1.itemconfigure(b,text="enter password")
                
            else:
                try:
                    global uid
                    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="stocks")
                    con=mydb.cursor()
                    con.execute("select password from login where email=%s",(eid,))
                    result=con.fetchone()
                    con.execute("select uid from shareholder where email=%s",(eid,))
                    uid=con.fetchone()
                    mydb.close()
                    if(result[0]!=p):
                        myc1.itemconfigure(b,text="Wrong password")
                    else:
                        messagebox.showinfo("login","login successfull")
                        root1.destroy()
                        stock(r,uid[0])
                except :
                    myc1.itemconfigure(a,text="Email not found")

        else :
            myc1.itemconfigure(a,text="enter valid email")
           
    def email(e):
        myc1.itemconfigure(a,text="")
        if(em.get()=="Email"):
            em.delete(0,END)
            em.configure(fg="black")
        if(pw.get()==""):
            pw.configure(show="",fg="grey")
            pw.insert(0,"Password")
    def pwd(e):
        myc1.itemconfigure(b,text="")
        if(pw.get()=="Password"):
            pw.delete(0,END)
            pw.configure(show="*",fg="black")
        if(em.get()==""):
            em.configure(fg="grey")
            em.insert(0,"Email")

    em.bind("<Button-1>",email)
    pw.bind("<Button-1>",pwd)
    
    signin=Button(myc1,text="Sign In",bg="red",fg="White",height=0,width=7,font="times 17 bold",command=signin1)
    signin.place(x=452,y=450)
    myc1.create_text(385,530,text="New user? Sign Up!",anchor="nw",font="times 22 bold",fill="white")
    def signu():
        root1.withdraw()
        signup2(root1)
    signup=Button(myc1,text="Sign Up",bg="green",fg="White",height=0,width=7,font="times 17 bold",command=signu)
    signup.place(x=452,y=600)
    root1.mainloop()
