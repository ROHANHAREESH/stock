
from tkinter import *
screen = Tk()

frame1 = Frame(screen, borderwidth=5)
frame1.pack(side='right',fill=Y,pady=100)
frame1.config(width=600)

frame2 = Frame(screen, highlightbackground="black", highlightthickness=2)
frame2.pack(side='left',fill=Y)
frame2.config(width=300)

def register_user():

  username_info = username.get()
  password_info = password.get()

  file=open(username_info+".txt", "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(frame1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()

def register():

  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(frame1, text = "Please enter details below",padx=225,pady=0).pack(side=TOP)
  Label(frame1, text = "").pack()
  Label(frame1, text = "EMail* ").pack()
  username_entry = Entry(frame1, textvariable = username)
  username_entry.pack()
  Label(frame1, text = "Password * ").pack()
  password_entry =  Entry(frame1, textvariable = password)
  password_entry.pack()
  Label(frame1, text = "").pack()
  Button(frame1, text = "Register", width = 10, height = 1, command = register_user).pack()
  Button(frame1, text = "Register", width = 10, height = 1, command = frame2).pack()
def login():
  print("Login session started")


def main_screen():
  global screen
  
  screen.geometry("800x800")
  screen.title("Trading App")
  Label(frame2,text = "Welcome!!", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(frame2,text = "").pack()
  button1 = Button(frame2,text = "Login", height = "1", width = "10", command = login).pack()
  
  #Label(frame2,text = "").pack()
  button2=Button(frame2,text = "Register",height = "1", width = "10", command = register).pack()
  Button(frame2, text = "EXIT", width = 10, height = 1, command = screen.destroy).pack(side=BOTTOM,pady=10)

  screen.mainloop()

main_screen()
  