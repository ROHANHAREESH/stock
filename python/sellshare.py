from tkinter import *
from PIL import Image,ImageTk
from bs4 import BeautifulSoup as bs
from tkinter import messagebox
import requests
import traceback
import mysql.connector
import datetime
import pytz
def sells(r,s,res,uid):
    root2=Toplevel()
    root2.geometry('1000x720+250+50')
    root2.resizable(0,0)
    bgg=ImageTk.PhotoImage(file="images\stk2.jpg")
    myc1=Canvas(root2,width=1000,height=720,bd=0,highlightthickness=0)
    myc1.pack(fill='both',expand=True)
    myc1.create_image(0,0,image=bgg,anchor="nw")

    h=myc1.create_text(150,80,text="",anchor="nw",font="times 24 bold underline",fill="white")
    lt=myc1.create_text(205,190,text="",anchor="nw",font="times 30 bold underline",fill="white")
    cp=myc1.create_text(205,270,text="",anchor="nw",font="times 30 bold underline",fill="white")
    porl=myc1.create_text(205,440,text="",anchor="nw",font="times 30 bold underline",fill="white")
    tporl=myc1.create_text(205,520,text="",anchor="nw",font="times 30 bold underline",fill="white")
    costp=res[2]
    quan=res[3]
    myc1.create_text(750,150,text="Shares : "+str(quan),anchor="nw",font="times 25 bold underline",fill="white")
    def get(s):
        global iltp,tax,totamt,head,qt
        link="https://www.google.com/finance/quote/"+s+":NSE"
        page=requests.get(link)
        soup=bs(page.content,'lxml')
        ltp=soup.find('div',class_="YMlKec fxKbKc").text
        head=soup.find('h1',class_="zzDege").text
        iltp=float(ltp.replace('\u20B9','').replace(',',''))
        myc1.itemconfigure(h,text=head)
        myc1.itemconfigure(lt,text="Sell Price : "+'\u20B9'+str(iltp))
        qt=1
        p=(iltp-costp)
        tp=p
        if(p>0):
            myc1.itemconfigure(porl,fill="#00FF00",text="Profit/share : "+'\u20B9'+str(p))
            myc1.itemconfigure(tporl,fill="#00FF00",text="Total Profit : "+'\u20B9'+str(tp))
        else:
            myc1.itemconfigure(porl,fill="red",text="Loss/share : "+'\u20B9'+str(p))
            myc1.itemconfigure(tporl,fill="red",text="Total Loss : "+'\u20B9'+str(tp))

    get(s)
    def scalc():
        get(s)
        global qt
        qt=int(quantity.get())
        if(qt>quan):
            messagebox.showerror("error","NOT ENOUGH SHARES")
        else:
            p=(iltp-costp)
            tp=p*qt
            if(p>0):
                myc1.itemconfigure(porl,fill="#00FF00",text="Profit/share : "+'\u20B9'+str(p))
                myc1.itemconfigure(tporl,fill="#00FF00",text="Total Profit : "+'\u20B9'+str(tp))
            else:
                myc1.itemconfigure(porl,fill="red",text="Loss/share : "+'\u20B9'+str(p))
                myc1.itemconfigure(tporl,fill="red",text="Total Loss : "+'\u20B9'+str(tp))
    myc1.itemconfigure(cp,text="Cost Price : "+'\u20B9'+str(costp))
    quantity=Spinbox(myc1,from_=1,to=quan,font="times 18 bold",command=scalc)
    quantity.place(x=480,y=365)
    myc1.create_text(204,355,text="Shares to sell : ",anchor="nw",font="times 30 bold underline",fill="white")
    
    
    def sellshare():
        try:
            c=datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%d-%m-%y %H:%M:%S')
            mydb=mysql.connector.connect(host="localhost",user="root",password="",database="stocks")
            con=mydb.cursor()
            con.execute("select w_amt from wallet where uid=%s order by no desc limit 1",(uid,))
            wallet=con.fetchone()
            rq=quan-qt
            if(rq==0):
                con.execute("delete from shares  where uid=%s and sname=%s",(uid,head))
            else:
                con.execute("update shares set squantity=%s where uid=%s and sname=%s",(rq,uid,head))
            tamt=iltp*qt
            tamt=iltp*qt
            neww=wallet[0]+tamt
            con.execute("insert into wallet(uid,w_amt,debit,credit,time)values(%s,%s,%s,%s,%s)",(uid,neww,0,tamt,c))
            mydb.commit()
            messagebox.showinfo("sell","SHARES SOLD")
            back()
        except:
            traceback.print_exc()
    sell=Button(myc1,text="Sell",bg="red",fg="White",height=0,width=15,font="times 18 bold",command=sellshare)
    sell.place(x=350,y=610)
    btnim=ImageTk.PhotoImage(file="images\\back.png")
    def back():
        root2.destroy()
        r.deiconify()
    btn=Button(myc1,image=btnim,bg="white",command=back)
    btn.place(x=30,y=30)
    root2.mainloop()
