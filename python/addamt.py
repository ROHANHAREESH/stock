from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pytz
import datetime
import mysql.connector
def addamt(uid):
    root2=Toplevel()
    root2.geometry('500x360+500+200')
    root2.resizable(0,0)
    bgg=ImageTk.PhotoImage(file="images\stk2.jpg")
    myc1=Canvas(root2,width=500,height=360,bd=0,highlightthickness=0)
    myc1.pack(fill='both',expand=True)
    myc1.create_image(0,0,image=bgg,anchor="nw")
    myc1.create_text(120,70,text="Enter Amount : ",anchor="nw",font="times 25 bold",fill="white")
    amt=Entry(myc1,font="times 20 ",fg="black",width=20)
    amt.place(x=120,y=150)
        
    def ad():
        try:
            c=datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%d-%m-%y %H:%M:%S')
            wa=int(amt.get())
            mydb=mysql.connector.connect(host="localhost",user="root",password="",database="stocks")
            con=mydb.cursor()
            con.execute("select w_amt from wallet where uid=%s order by no desc limit 1",(uid,))
            wallet=con.fetchone()
            neww=wallet[0]+wa
            con.execute("insert into wallet(uid,w_amt,debit,credit,time)values(%s,%s,%s,%s,%s)",(uid,neww,0,wa,c))
            mydb.commit()
            messagebox.showinfo("success","AMOUNT SUCCESSFULLY ADDED")
            root2.destroy()
            mydb.close()
        except:
            traceback.print_exc()
    w=Button(myc1,text="Add",bg="red",fg="White",height=0,width=8,font="times 15 bold",command=ad)
    w.place(x=200,y=220)
    root2.mainloop()
