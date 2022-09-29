from tkinter import *
from PIL import ImageTk,Image
import pyttsx3
import time
from win32api import GetSystemMetrics

'''----------------------------------------------------------------------------------------------------'''
#screen
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
'''----------------------------------------------------------------------------------------------------'''

root=Tk()
root.overrideredirect(True)
root.geometry(f"{width}x{height}")
engine = pyttsx3.init()
engine.setProperty('rate', 140)
t= int(time.strftime('%H'))
if t > 12 :
     engine.say("Good Afternoon, This Project Is Made By Deepesh Kumar")
     engine.runAndWait()
elif t < 12 :
     engine.say("Good Morning, This Project Is Made By Deepesh Kumar")
     engine.runAndWait()
else :
     engine.say("Good Evening, This Project Is Made By Deepesh Kumar")
     engine.runAndWait()

background_image=ImageTk.PhotoImage(file="my_back.jpg")
background_label = Label(root,image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


ml="""Mr. Meena Sir
He is my teacher teaches me computer science from class 11 KVS Delhi Cantt
He inspired me to make this project and guided/helped me and my project
pratners to do something like this infact he helped the whole class to
make there projects. So I just want to Thanks him for this help."""
def sir(s):
     root1=Tk()
     root1.title("About My Inspiration")
     root1.configure(bg="grey6")
     f= LabelFrame(root1,padx=20,pady=20)
     f.pack(padx=40,pady=40)
     l=Label(f,text=ml,bg="grey6",fg="cyan",font=("arial",10))
     l.pack()
     root1.after(22000,root1.destroy)
def team(d):
     root1=Toplevel()
     root1.geometry("1200x700+83+10")
     root1.configure(bg="grey4")
     root1.overrideredirect(True)
     def team1(e):
          global im
          global im1
          global im2
          global photo
          global photo1
          global photo2
          global photo3
          im=ImageTk.PhotoImage(file="back2.jpg")
          im1=ImageTk.PhotoImage(file="back1.jpg")
          im2=ImageTk.PhotoImage(file="back4.jpg")
          a=[im,im1,im2]
          lab = Label(root1,image=a[e-1])
          lab.place(x=0, y=0)
          photo=ImageTk.PhotoImage(file="deepesh.jpg")
          l=Label(root1,image=photo)
          l.place(x=10,y=10)
          Label(root1,text="Deepesh Kumar\nClass 12A",bg="grey4",fg="lightgreen",borderwidth=0).place(x=70,y=305)

          photo3=ImageTk.PhotoImage(file="himanshu.jpg")
          l3=Label(root1,image=photo3)
          l3.place(x=100,y=350)
          Label(root1,text="Himanshu Dixit\nClass 12A",bg="grey4",fg="lightgreen",borderwidth=0).place(x=210,y=650)

          photo1=ImageTk.PhotoImage(file="surya.jpg")
          l1=Label(root1,image=photo1)
          l1.place(x=280,y=10)
          Label(root1,text="Surya Kant Verma\nClass 12A",bg="grey4",fg="lightgreen",borderwidth=0).place(x=300,y=215)

          photo2=ImageTk.PhotoImage(file="sir.jpg")
          l2=Label(root1,image=photo2)
          l2.place(x=490,y=80)
          Label(root1,text="Mr. ML\n Meena Sir",bg="grey4",fg="lightgreen",borderwidth=0).place(x=785,y=560)

     root.after(0,lambda :team1(1))
     root.after(3300,lambda :team1(2))
     root.after(6600,lambda :team1(3))
     root1.after(10000,root1.destroy)

def s():
     global img
     root1=Toplevel()
     root1.overrideredirect(True)
     root1.geometry("+671+470")#440,289
     img=ImageTk.PhotoImage(file="s.jpg")
     l=Label(root1,image=img)
     l.pack()
     root1.after(7000,root1.destroy)
def d():
     global img1
     root1=Toplevel()
     root1.overrideredirect(True)
     root1.geometry("+816+501")
     img1=ImageTk.PhotoImage(file="d.jpg")
     l=Label(root1,image=img1)
     l.pack()
     root1.after(7000,root1.destroy)
def m():
     global i1
     root1=Toplevel()
     root1.overrideredirect(True)
     root1.geometry("+962+501")
     i1=ImageTk.PhotoImage(file="m.jpg")
     l=Label(root1,image=i1)
     l.pack()
     root1.after(7000,root1.destroy)
def s1():
     global i
     root1=Toplevel()
     root1.overrideredirect(True)
     root1.geometry("+1105+470")
     i=ImageTk.PhotoImage(file="s.jpg")
     l=Label(root1,image=i)
     l.pack()
     root1.after(7000,root1.destroy)
def s2():
     engine.say("S,D,M,S, Security is Prriorritty..")
     engine.runAndWait()
     global i2
     root1=Toplevel()
     root1.overrideredirect(True)
     root1.geometry("+793+340")
     i2=ImageTk.PhotoImage(file="sdms1.png")
     l=Label(root1,image=i2)
     l.pack()
     root1.after(7000,root1.destroy)
root.after(2000,s)
root.after(3000,d)
root.after(4000,m)
root.after(5000,s1)
root.after(14000,s2)

a="""This is a virtual bank transaction project made by Deepesh Kumar , Surya Kant Verma and Himanshu Dixit
Actually this project works with DBMS (Data Base Management System) and python connected by mysql.connector
     In this project you can:-
     \a1)=Create Account
     \a2)=Deposit Money
     \a3)=Withdraw Money
     \a4)=Display an Account
     \a5)=Transfer Money
     \a6)=See All Accounts
And everything will be saved as an Database 
     Thanks For Seeing Our Project"""
def about(z):
     root1=Tk()
     root1.title("About Project")
     root1.geometry("+210+200")
     root1.overrideredirect(True)
     root1.configure(bg="black")
     f= LabelFrame(root1,text="About Our Project",bg="yellow",fg="green",padx=20,pady=20)
     f.pack(padx=40,pady=40)
     l=Label(f,text=a,bg="red",fg="yellow",font=("arial",10),justify=LEFT)
     l.pack()
     root1.after(26000,root1.destroy)

def ab(x):     
     engine.say(a)
     engine.runAndWait()

bt="""OPENING SCREEN:- 
1) tkinter                - For making the opening screen(Buttons, frame, ect)
2) PIL or pillow      -For putting images on the screen 
3) pyttsx3               -For auto generated voice 
4) time                   -For saying good morning, good evening,etc at correct time    """
ct="""MAIN PROJECT:-
1) tkinter                   ~For making the login page of mysql
2)time                       ~For waiting(loading), to be more realistic
3) mysql.connector    ~For everything to be saved as a database for future
4)sys                          ~For exit programm if username or password of mysql is wrong """
def cd(y):   
     engine.say(bt)
     engine.say(ct)
     engine.runAndWait()     
def module(m):
     root1=Tk()
     root1.title("Modules Used")
     root1.overrideredirect(True)
     root1.geometry("+10+30")
     root1.configure(bg="black")
     f= LabelFrame(root1,text="These Are The Modules We Use",bg="yellow",fg="green",padx=20,pady=20)
     f.pack(padx=20,pady=40)
     f1= LabelFrame(root1,padx=20,pady=20)
     f1.pack(padx=10,side=RIGHT)
     l1=Label(f,text=ct,bg="cyan",fg="red",font=("arial",10),justify=LEFT)
     l1.pack(side="right",padx=10)
     l=Label(f,text=bt,bg="red",fg="yellow",font=("arial",10),justify=LEFT)
     l.pack()
     root1.after(27000,root1.destroy)
def close(a):
     root.destroy()

ti="""1)You can access whole project with help of your keyboard only:-
Just Press 'a' to see 'ABOUT PROJECT'
m for Modules Used
t for project team
and press enter to enter in main project

2) Theres a feedback option at last of project but
it only arises if you click no when I ask you
"Do you like project" So just press yes there if
you don't want to give any feedback

3)The Photos At The Corners Can be Clicked

4)About Project, modules used, these tips all will be speaked
if you just press there second letters of them for eg : for tips press i

6)SDMS name comes from Team members
S :- Surya kant
D:- Deepesh
MS:- Ml Meena Sir

\a I said that you can access whole project with keyboard
but you can't see tips with your keyboard. ha ha ha"""
def ef(w):   
     engine.say(ti)
     engine.runAndWait()
def tips():
     root1=Tk()
     root1.title("Tricks In The Project")
     root1.configure(bg="grey5")
     f= LabelFrame(root1,padx=20,pady=20)
     f.pack(padx=40,pady=40)
     l=Label(f,text=ti,bg="grey5",fg="cyan",font=("arial",10),justify=LEFT)
     l.pack()
     root1.after(48000,root1.destroy)
root.bind('<t>',team)
root.bind('<a>',about)
root.bind('<m>',module)
root.bind('<Return>',close)
root.bind('<s>',sir)
root.bind('<b>',ab)
root.bind('<o>',cd)
root.bind('<i>',ef)

btn1=ImageTk.PhotoImage(file="sdms.png")
b=Button(root,image=btn1,command=root.destroy,borderwidth=10,bg="blue",activebackground="red").place(relx=0.5, rely=0.5, anchor=CENTER)

b1=Button(root,text="ABOUT PROJECT",bg="grey19",fg="greenyellow",activebackground="greenyellow",activeforeground="grey19",command=lambda: about(1))
b1.place(x=1800,y=300)

b2=Button(root,text="MODULES USED",bg="grey19",fg="greenyellow",activebackground="greenyellow",activeforeground="grey19",command=lambda: module(1))
b2.place(x=0,y=300)
btn=ImageTk.PhotoImage(file="sir1.jpg")
b5=Button(root,image=btn,command=lambda: sir(1),borderwidth=0).place(x=0,y=888)

btn2=ImageTk.PhotoImage(file="team.png")
b3=Button(root,image=btn2,borderwidth=0,command=lambda: team(1))
b3.place(x=1800,y=977)

b4=Button(root,text="Tips And Tricks",bg="grey19",fg="greenyellow",activebackground="greenyellow",activeforeground="grey19",command=tips).place(x=0,y=690)
def auto(p):
     engine.say("Presenting")
     engine.runAndWait()
     root.after(1000,lambda: about(1))
     root.after(28000,lambda: module(1))
     root.after(56000,tips)
     root.after(105000,lambda: sir(1))
     root.after(128000,lambda: team(1))     
     root.after(140000,root.destroy)
root.bind('<p>',auto)

btn3=ImageTk.PhotoImage(file="play1.png")
b6=Button(root,image=btn3,command=lambda: auto(1),borderwidth=10,bg="grey6").place(x=890,y=963)

root.mainloop()
engine.say("Kindly Enter Your Username And password of S Q L")
engine.runAndWait()

import Bank_Project
