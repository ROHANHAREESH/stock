from tkinter import *
from PIL import Image,ImageTk
from bs4 import BeautifulSoup as bs
from tkinter import messagebox
import requests
import traceback
import mysql.connector
import datetime
import pytz
def buys(r,s,uid):
    root2=Toplevel()
    root2.geometry('1000x720+250+50')
    root2.resizable(0,0)
    bgg=ImageTk.PhotoImage(file="images\stk2.jpg")
    myc1=Canvas(root2,width=1000,height=720,bd=0,highlightthickness=0)
    myc1.pack(fill='both',expand=True)
    myc1.create_image(0,0,image=bgg,anchor="nw")

    h=myc1.create_text(150,80,text="",anchor="nw",font="times 24 bold underline",fill="white")
    lt=myc1.create_text(250,150,text="",anchor="nw",font="times 40 bold underline",fill="white")
    inc=myc1.create_text(492,170,text="",anchor="nw",font="times 18 bold",fill="white")
    sh=myc1.create_text(205,350,text="",anchor="nw",font="times 30 bold underline",fill="white")
    tx=myc1.create_text(205,440,text="",anchor="nw",font="times 30 bold underline",fill="white")
    tot=myc1.create_text(205,520,text="",anchor="nw",font="times 30 bold underline",fill="white")
    def get(s):
        global iltp,tax,totamt,head,qty
        link="https://www.google.com/finance/quote/"+s+":NSE"
        page=requests.get(link)
        soup=bs(page.content,'lxml')
        ltp=soup.find('div',class_="YMlKec fxKbKc").text
        head=soup.find('h1',class_="zzDege").text
        pre=soup.find('div',class_="P6K39c").text
        iltp=float(ltp.replace('\u20B9','').replace(',',''))
        ipre=float(pre.replace('\u20B9','').replace(',',''))
        res=round((iltp-ipre),2)
        qty=1
        tax=round(((iltp*0.05)/100),2)
        totamt=round((iltp+tax),2)
        myc1.itemconfigure(h,text=head)
        myc1.itemconfigure(lt,text=ltp)
        if(res>0):
            myc1.itemconfigure(inc,fill="#00FF00",text="+"+str(res)+"  Today")
        else:
            myc1.itemconfigure(inc,fill="red",text=str(res)+"  Today")
        myc1.itemconfigure(sh,text="Share Amount : "+'\u20B9'+str(iltp))
        myc1.itemconfigure(tx,text="Tax : "+'\u20B9'+str(tax))
        myc1.itemconfigure(tot,text="Amount Payable : "+'\u20B9'+str(totamt))
    get(s)
    def calc(e):
        get(s)
        global qty,amt,totamt
        qty=int(quantity.get())
        amt=round((iltp*qty),2)
        tax=round(((0.05*amt)/100),2)
        totamt=round((amt+tax),2)
        myc1.itemconfigure(sh,text="Share Amount : "+'\u20B9'+str(amt))
        myc1.itemconfigure(tx,text="Tax : "+'\u20B9'+str(tax))
        myc1.itemconfigure(tot,text="Amount Payable : "+'\u20B9'+str(totamt))
    quantity=Spinbox(myc1,from_=1,to=100,font="times 18 bold",command=lambda :calc(0))
    quantity.place(x=380,y=280)
    quantity.bind('<Return>',calc)
    myc1.create_text(204,270,text="Buy Qty :",anchor="nw",font="times 30 bold underline",fill="white")
    btnim=ImageTk.PhotoImage(file="images\\back.png")
    def back():
        root2.destroy()
        r.deiconify()
    btn=Button(myc1,image=btnim,bg="white",command=back)
    btn.place(x=30,y=30)
    def buyshare():
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",password="",database="stocks")
            con=mydb.cursor()
            con.execute("select w_amt from wallet where uid=%s order by no desc limit 1",(uid,))
            userid=con.fetchone()
            mydb.close()
            if(userid[0]<totamt):
                messagebox.showwarning("balance","INSUFFICIENT BALANCE ")
            else:
                p=messagebox.askokcancel("confirmation","CONFIRM TRANSACTION ?")
                if(p):
                    c=datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%d-%m-%y %H:%M:%S')
                    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="stocks")
                    con=mydb.cursor()
                    con.execute("insert into shares(uid,sname,ssymbol,sprice,squantity,tot_amt,trans_time)values(%s,%s,%s,%s,%s,%s,%s)",(uid,head,s,iltp,qty,totamt,c))
                    neww=userid[0]-totamt
                    con.execute("insert into wallet(uid,w_amt,debit,credit,time)values(%s,%s,%s,%s,%s)",(uid,neww,totamt,0,c))
                    mydb.commit()
                    messagebox.showinfo("success","Transaction successfull")
                    

        except:
            traceback.print_exc()
    buy=Button(myc1,text="Buy",bg="green",fg="White",height=0,width=15,font="times 18 bold",command=buyshare)
    buy.place(x=350,y=610)
    root2.mainloop()