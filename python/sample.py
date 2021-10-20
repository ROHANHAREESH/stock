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
root2=Tk()
root2.geometry('1000x720+250+50')
root2.resizable(0,0)
bgg=ImageTk.PhotoImage(file="stk2.jpg")
myc1=Canvas(root2,width=1000,height=720,bd=0,highlightthickness=0)
myc1.pack(fill='both',expand=True)
myc1.create_image(0,0,image=bgg,anchor="nw")
ct=0

b={}
for i in range(3):
    ct=ct+100
    def show(x=i):
        print(x)
    b[i]=Button(myc1,text="view",bg="green",fg="White",height=0,width=6,font="times 20 bold",command=show).place(x=800,y=ct+50)

root2.mainloop()
