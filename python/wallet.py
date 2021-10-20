from tkinter import *
from PIL import Image,ImageTk
from bs4 import BeautifulSoup as bs
from tkinter import messagebox
from lostocks2 import stock2
from trans import tra
from addamt import addamt
import requests
import traceback
import mysql.connector
import datetime
import pytz
def wall(r,uid):
    root2=Toplevel()
    root2.geometry('1000x720+250+50')
    root2.resizable(0,0)
    bgg=ImageTk.PhotoImage(file="images\stk2.jpg")
    myc1=Canvas(root2,width=1000,height=720,bd=0,highlightthickness=0)
    myc1.pack(fill='both',expand=True)
    myc1.create_image(0,0,image=bgg,anchor="nw")
    bal=myc1.create_text(350,70,text="",anchor="nw",font="times 40 bold",fill="white")
    def rwall():
        myc1.create_text(400,30,text="Balance",anchor="nw",font="times 24 bold underline",fill="white")
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",password="",database="stocks")
            con=mydb.cursor()
            con.execute("select w_amt from wallet where uid=%s order by no desc limit 1",(uid,))
            wallet=con.fetchone()
            myc1.itemconfigure(bal,text='\u20B9'+str(wallet[0]))
            con.execute("select * from shares where uid=%s",(uid,))
            share=con.fetchall()
            myc1.create_text(350,170,text="Shares Held",anchor="nw",font="times 30 bold underline",fill="white")
            ct=150
            for i in share:
                def wsell(ti=i):
                    root2.withdraw()
                    stock2(root2,ti[6],uid)
                ct=ct+100
                myc1.create_text(120,ct,text=i[1],anchor="nw",font="times 30 bold",fill="white")
                myc1.create_text(120,ct+40,text=i[5],anchor="nw",font="times 15 bold",fill="white")
                myc1.create_text(650,ct+10,text="shares : "+str(i[3]),anchor="nw",font="times 20 bold",fill="white")
                Button(myc1,text="view",bg="green",fg="White",height=0,width=6,font="times 20 bold",command=wsell).place(x=800,y=ct+10)
        except:
            traceback.print_exc()
        def tranc():
            root2.withdraw()
            tra(root2,uid)
        thistory=Button(myc1,text="Transactions",bg="red",fg="White",height=0,width=10,font="times 15 bold",command=tranc)
        thistory.place(x=850,y=100)
    btnim=ImageTk.PhotoImage(file="images\\back.png")
    def back():
        root2.destroy()
        r.deiconify()
    btn1=Button(myc1,image=btnim,bg="white",command=back)
    btn1.place(x=30,y=30)
    def add1():
        addamt(uid)
    btnim1=ImageTk.PhotoImage(file="images\\add.png")
    btn=Button(myc1,image=btnim1,bg="white",command=add1)
    btn.place(x=600,y=70)
    rwall()    
    root2.mainloop()

