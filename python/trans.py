from tkinter import *
from PIL import Image,ImageTk
from bs4 import BeautifulSoup as bs
from tkinter import messagebox
import requests
import traceback
import mysql.connector
import datetime
import pytz
def tra(r,uid):
    root2=Toplevel()
    root2.geometry('1000x720+250+50')
    root2.resizable(0,0)
    bgg=ImageTk.PhotoImage(file="images\stk2.jpg")
    myc1=Canvas(root2,width=1000,height=720,bd=0,highlightthickness=0)
    myc1.pack(fill='both',expand=True)
    myc1.create_image(0,0,image=bgg,anchor="nw")

    myc1.create_text(400,30,text="Balance",anchor="nw",font="times 24 bold underline",fill="white")
    myc1.create_text(320,180,text="Transaction Details",anchor="nw",font="times 25 bold underline",fill="white")
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="",database="stocks")
        con=mydb.cursor()
        con.execute("select w_amt from wallet where uid=%s order by no desc limit 1",(uid,))
        wallet=con.fetchone()
        myc1.create_text(350,70,text='\u20B9'+str(wallet[0]),anchor="nw",font="times 40 bold",fill="white")
        con.execute("select * from wallet where uid=%s",(uid,))
        trans=con.fetchall()
        Label(myc1,text="Balance",bg="white",bd=4,width=13,font="times 18 bold underline").place(x=100,y=250)
        Label(myc1,text="Debit",bg="white",bd=4,width=13,font="times 18 bold").place(x=300,y=250)
        Label(myc1,text="Credit",bg="white",bd=4,width=13,font="times 18 bold").place(x=500,y=250)
        Label(myc1,text="Trans_time",bg="white",bd=4,width=13,font="times 18 bold").place(x=700,y=250)

        ct=-100
        ct1=250
        for i in range(len(trans)):
            ct1=ct1+40
            ct=-100
            for j in range(1,5):
                ct=ct+200
                if(j==2):
                    Label(myc1,text='\u20B9'+str(trans[i][j]),bg="white",fg="red",bd=4,width=14,font="times 18 ").place(x=ct,y=ct1)
                elif(j==3):
                    Label(myc1,text='\u20B9'+str(trans[i][j]),bg="white",fg="green",bd=4,width=14,font="times 18 ").place(x=ct,y=ct1)
                elif(j==4):
                    Label(myc1,text=str(trans[i][j]),bg="white",fg="black",bd=4,width=14,font="times 18 ").place(x=ct,y=ct1)
                else:
                    Label(myc1,text='\u20B9'+str(trans[i][j]),bg="white",fg="black",bd=4,width=14,font="times 18 ").place(x=ct,y=ct1)
               # myc1.create_text(ct,ct1,text="Bal",anchor="nw",font="times 24 bold ",fill="black")
    except:
        traceback.print_exc()
    btnim=ImageTk.PhotoImage(file="images\\back.png")
    def back():
        root2.destroy()
        r.deiconify()
    btn=Button(myc1,image=btnim,bg="white",command=back)
    btn.place(x=30,y=30)
    root2.mainloop()
