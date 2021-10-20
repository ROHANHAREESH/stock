from tkinter import *
from PIL import Image,ImageTk
from bs4 import BeautifulSoup as bs
import requests
def stock2(r,s):
    root2=Toplevel()
    root2.geometry('1000x720+250+50')
    root2.resizable(0,0)
    bgg=ImageTk.PhotoImage(file="images\stk2.jpg")
    myc1=Canvas(root2,width=1000,height=720,bd=0,highlightthickness=0)
    myc1.pack(fill='both',expand=True)
    myc1.create_image(0,0,image=bgg,anchor="nw")

    #labels
    h=myc1.create_text(150,80,text="",anchor="nw",font="times 24 bold underline",fill="white")
    lt=myc1.create_text(200,150,text="",anchor="nw",font="times 40 bold underline",fill="white")
    inc=myc1.create_text(452,170,text="",anchor="nw",font="times 18 bold",fill="white")
    pclo=myc1.create_text(120,280,text="",anchor="nw",font="times 23 bold underline ",fill="white")
    pr=myc1.create_text(580,280,text="",anchor="nw",font="times 23 bold underline ",fill="white")
    dl=myc1.create_text(120,370,text="",anchor="nw",font="times 23 bold underline ",fill="white")
    dh=myc1.create_text(580,370,text="",anchor="nw",font="times 23 bold underline ",fill="white")
    yrl=myc1.create_text(120,450,text="",anchor="nw",font="times 23 bold underline ",fill="white")
    yrh=myc1.create_text(580,450,text="",anchor="nw",font="times 23 bold underline ",fill="white")
    capi=myc1.create_text(120,530,text="",anchor="nw",font="times 23 bold underline ",fill="white")
    di=myc1.create_text(580,530,text="",anchor="nw",font="times 23 bold underline ",fill="white")
    def back():
        root2.destroy()
        r.deiconify()
    btnim=ImageTk.PhotoImage(file="images\\back.png")
    btn=Button(myc1,image=btnim,bg="white",command=back)
    btn.place(x=30,y=30)
    def get(s):
        link="https://www.google.com/finance/quote/"+s+":NSE"
        page=requests.get(link)
        soup=bs(page.content,'lxml')
        ltp=soup.find('div',class_="YMlKec fxKbKc").text
        pre=soup.find_all('div',class_="P6K39c")
        head=soup.find('h1',class_="zzDege").text
        prev=pre[0].text
        dayL=pre[1].text.partition('-')[0]
        dayH=pre[1].text.partition('-')[2]
        yL=pre[2].text.partition('-')[0]
        yH=pre[2].text.partition('-')[2]
        cap=pre[3].text
        PE=pre[4].text
        div=pre[5].text
        iltp=float(ltp.replace('\u20B9','').replace(',',''))
        ipre=float(prev.replace('\u20B9','').replace(',',''))
        res=round((iltp-ipre),2)
        if(res>0):
            myc1.itemconfigure(inc,fill="#00FF00",text="+"+str(res)+"  Today")
        else:
            myc1.itemconfigure(inc,fill="red",text=str(res)+"  Today")
        myc1.itemconfigure(h,text=head)
        myc1.itemconfigure(lt,text=ltp)
        myc1.itemconfigure(pclo,text="Prev close    :  "+prev)
        myc1.itemconfigure(pr,text="P/E ratio      :   "+PE)
        myc1.itemconfigure(dl,text="DailyLow     :  "+dayL)
        myc1.itemconfigure(dh,text="DailyHigh     :  "+dayH)
        myc1.itemconfigure(yrl,text="52WeekLow :  "+yL)
        myc1.itemconfigure(yrh,text="52WeekHigh :  "+yH)
        myc1.itemconfigure(capi,text="MarketCap :  "+cap)
        myc1.itemconfigure(di,text="DividendYield :  "+div)
    get(s)
    rf=ImageTk.PhotoImage(file="images\\refresh.png")
    refreh=Button(myc1,text="Refresh",image=rf,compound=LEFT,bg="white",fg="blue",font="times 17 bold",command=lambda :get(s))
    refreh.place(x=450,y=20)
    root2.mainloop()

    