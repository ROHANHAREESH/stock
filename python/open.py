from tkinter import *
from PIL import ImageTk,Image
from login import log
from stocks import stock
def open1():
    root=Tk()
    root.geometry('1000x720+250+50')
    root.resizable(0,0)
    bg=ImageTk.PhotoImage(file="images\stck4.jpg")

    myc=Canvas(root,width=1000,height=720)
    myc.pack(fill='both',expand=True)
    myc.create_image(0,0,image=bg,anchor="nw")
    quote=u'\u201C'+" Stock market is a device to trasfer\n money from the impatient\n to the patient "+u'\u201D'+"\n\t\t-Warren Buffet"
    myc.create_text(50,100,text=quote,anchor="nw",font='times 35 bold italic',fill="white")
    def lo():
        root.withdraw()
        log(root)
    def view():
        root.withdraw()
        stock(root)
    l=Button(myc,text="Sign In",bg="red",fg="white",width=12,height=1,font="times 20 bold",command=lo)
    l.place(x=700,y=400)
    st=Button(myc,text="view stocks",bg="red",fg="white",width=12,height=1,font="times 20 bold",command=view)
    st.place(x=700,y=500)
    root.mainloop()
open1()