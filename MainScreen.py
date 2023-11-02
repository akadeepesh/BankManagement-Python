import time
import sys
import os

"""----------------------------------------------------------------------------------------------------"""
# Installing modules if not installed
try:
    import PIL
except ImportError as e:
    os.system('cmd /c "pip install pillow"')

try:
    import mysql.connector
except ImportError as e:
    os.system('cmd /c "pip install mysql-connector-python"')

try:
    from art import *
except ImportError as e:
    os.system('cmd /c "pip install art"')

try:
    import pyttsx3
except ImportError as e:
    os.system('cmd /c "pip install pyttsx3"')
try:
    import pyglet
except ImportError as e:
    os.system('cmd /c "pip install pyglet"')

try:
    from win32api import GetSystemMetrics
except ImportError as e:
    os.system('cmd /c "pip install pypiwin32"')
"""----------------------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------------------"""
# importing modules
import mysql.connector
from datetime import date
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from art import *
import pyttsx3
from win32api import GetSystemMetrics
from itertools import count, cycle
import threading as th

"""----------------------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------------------"""
# engine variable to initialise pyttsx3 and set properties (say)
engine = pyttsx3.init()
engine.setProperty("rate", 140)
"""----------------------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------------------"""
# screen
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
win_width = 500
win_height = 300

mid_width = int(width / 2) - 250
"""----------------------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------------------"""
# Ascii art print
tprint("DC", font="doom")
print(14 * "=", ">")
engine.say("Welcome to DeCoder")
engine.runAndWait()
"""----------------------------------------------------------------------------------------------------"""

"""----------------------------------------------------------------------------------------------------"""
# Tkinter Sql window
root = Tk()
root.overrideredirect(True)
root.geometry(f"{win_width}x{win_height}+{mid_width}+165")
background_image = ImageTk.PhotoImage(file="Images\sql.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
frame = LabelFrame(root, padx=20, bg="grey5", borderwidth=0)
frame.pack(padx=10, pady=10)
frame1 = LabelFrame(root, padx=20, bg="grey5", borderwidth=0)
frame1.pack(padx=10, pady=10)
l = Label(frame, text="USERNAME:", bg="grey5", fg="cyan").grid(row=0, column=0, pady=20)
user = Entry(frame, width=20, bg="greenyellow", fg="grey5", relief=SUNKEN)
user.grid(row=0, column=1, padx=20, pady=20)
user.insert(0, "root")
l1 = Label(frame1, text="PASSWORD:", bg="grey5", fg="cyan").grid(
    row=0, column=0, pady=20
)
f = Entry(frame1, width=20, bg="greenyellow", fg="grey5", relief=SUNKEN, show="\a")
f.grid(row=0, column=1, padx=20, pady=20)
f.insert(0, "deepesh")
btn = PhotoImage(file="Images/Submit.png")
# img=Label(image=btn)
"""----------------------------------------------------------------------------------------------------"""


def load():
    """-------------------------------------"""
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    mid_width = int(width / 2) - 300
    win_width = 100
    win_height = 60
    # mid_width_block = mid_width+300-
    """-------------------------------------"""

    class ImageLabel(Label):
        """
        A Label that displays images, and plays them if they are gifs
        :im: A PIL Image instance or a string filename
        """

        def load(self, im):
            if isinstance(im, str):
                im = Image.open(im)
            frames = []

            try:
                for i in count(1):
                    frames.append(ImageTk.PhotoImage(im.copy()))
                    im.seek(i)
            except EOFError:
                pass
            self.frames = cycle(frames)

            try:
                self.delay = im.info["duration"]
            except:
                self.delay = 10

            if len(frames) == 1:
                self.config(image=next(self.frames))
            else:
                self.next_frame()

        def unload(self):
            self.config(image=None)
            self.frames = None

        def next_frame(self):
            if self.frames:
                self.config(image=next(self.frames))
                self.after(self.delay, self.next_frame)

    """------Main_Gif_Screen-----------------"""
    root = Toplevel()
    root.overrideredirect(1)
    root.geometry(f"+{mid_width}+165")
    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load("circle.gif")
    root.after(5000, lambda: root.destroy())
    """---------------------------------------"""
    """----------Top screen for text----------"""
    top = Toplevel()
    top.configure(bg="black")
    top.overrideredirect(1)
    top.geometry("200x40+860+485")
    top.lift(root)
    frame = LabelFrame(top, padx=40, bg="#181D24", borderwidth=0)
    frame.pack()
    l = Label(
        frame,
        text="Loading...",
        bg="#181D24",
        fg="white",
        font=("harlow solid italic", 17),
    ).grid(row=0, column=0)
    top.after(5000, lambda: top.destroy())
    """---------------------------------------"""
    top.mainloop()
    root.mainloop()


def conn():
    global date
    global mn
    userName = user.get()
    cd = f.get()
    try:
        mydb = mysql.connector.connect(host="localhost", user=userName, passwd=cd)
    except:
        root.destroy()
        print(
            "\nSoory But You Entered Wrong Username or Password,\nI Can't give you Acsess To Do Any Transactions"
        )
        print(f"\nYou Entered '{cd}' as your Password Kindly Recheck That")
        sys.exit()
    root.destroy()
    mycursor = mydb.cursor()
    mycursor.execute("create database if not exists bank")
    mycursor.execute("use bank")

    mycursor.execute(
        "create table if not exists bank_master(acno char(4) primary key,name varchar(30),city char(20),mobileno char(10),balance int(6))"
    )
    mycursor.execute(
        "create table if not exists banktrans(acno char (4),amount int(6),dot date,ttype char(1),foreign key (acno) references bank_master(acno))"
    )
    mydb.commit()
    commands = [
        "Enter Account Number",
        "Enter Name (Limit 35 Characters)",
        "Enter City Name",
        "Enter Mobile Number",
        "Enter Amount To Be Deposited",
        "Enter Amount To Be Withdrawn",
    ]
    colon = ":"
    while True:
        print(
            "____________________________________________________________________________________\n"
        )
        print("|", chr(272), chr(268), "|  -1)=Create Account")
        print("|", chr(272), chr(268), "|  -2)=Deposit Money")
        print("|", chr(272), chr(268), "|  -3)=Withdraw Money")
        print("|", chr(272), chr(268), "|  -4)=Display Account")
        print("|", chr(272), chr(268), "|  -5)=Transfer Money")
        print("|", chr(272), chr(268), "|  -6)=Show All Accounts")
        print("|", chr(272), chr(268), "|  -7)=Exit\n")
        print(
            "____________________________________________________________________________________\n"
        )
        ch = int(input("\bEnter Your Choice (1 | 2 | 3 | 4 | 5 | 6 | 7) :"))
        print(
            "____________________________________________________________________________________"
        )
        print("\n")

        if ch == 1:
            print("*All Information Prompted Are Mandatory To Be Filled")
            print(f"{commands[1]:>20}{colon:>20}")
            acno = input("Enter Account Number                   :")
            while len(acno) != 4:
                print("Please Use 4 Digit Acc. No.")
                acno = input("Enter Account Number                   :")

            name = input("Enter Name (Limit 35 Characters)   :")
            while len(name) >= 35:
                print("Please Use Your Short Name(max 35 letters)")
                name = input("Enter Name (Limit 35 Characters)   :")
            city = input("Enter City Name                             :")

            mn = input("Enter Mobile Number                     :")
            while mn[0:3] == "+91":
                print("No Need To Use +91")
                mn = input("Enter Mobile Number                     :")
            while len(mn) != 10:
                print("Mobile no. Should Be Of 10 Digits")
                mn = input("Enter Mobile Number                     :")
            balance = 0
            print("Uploading Your Data...")
            time.sleep(2)
            mycursor.execute(
                "insert into bank_master values('"
                + acno
                + "','"
                + name
                + "','"
                + city
                + "','"
                + mn
                + "','"
                + str(balance)
                + "')"
            )
            mydb.commit()
            print("Congratulations Your Account Is Successfully Created!!!!\n")

        elif ch == 2:
            acno = str(input("Enter Account Number             :"))
            mn = str(input("Enter Your Mobile No.             :"))
            mycursor.execute(
                "select exists(select * from bank_master where acno='" + acno + "')"
            )
            a = mycursor.fetchall()
            mycursor.execute(
                "select exists(select * from bank_master where mobileno='" + mn + "')"
            )
            b = mycursor.fetchall()
            for x in a:
                print("Checking Account No...")
                time.sleep(2)
                for y in b:
                    print("Checking Mobile No....")
                    time.sleep(2)
                    if x[0] == 1:
                        print("Account No. Verified.")
                        if y[0] == 1:
                            print("Mobile No. Verified.")
                            dp = int(input("Enter Amount To Be Deposited:"))
                            today = date.today()
                            dot = str(today.strftime("%y/%m/%d"))
                            ttype = "d"
                            mycursor.execute(
                                "insert into banktrans values('"
                                + acno
                                + "','"
                                + str(dp)
                                + "','"
                                + dot
                                + "','"
                                + ttype
                                + "')"
                            )
                            mycursor.execute(
                                "update bank_master set balance=balance+'"
                                + str(dp)
                                + "' where acno='"
                                + acno
                                + "'"
                            )
                            mydb.commit()
                            print(dp, "rupees Has Been Deposited Successully!!!\n")
                        else:
                            print("Mobile No. Is Incorrect\n")
                    else:
                        print("Account Dosent Exists\n")

        elif ch == 3:
            acno = str(input("Enter Account Number               :"))
            mn = str(input("Enter Your Mobile No.               :"))
            mycursor.execute(
                "select exists(select * from bank_master where acno='" + acno + "')"
            )
            a = mycursor.fetchall()
            mycursor.execute(
                "select exists(select * from bank_master where mobileno='" + mn + "')"
            )
            b = mycursor.fetchall()
            for x in a:
                print("Checking Account No...")
                time.sleep(2)
                for y in b:
                    print("Checking Mobile No....")
                    time.sleep(2)
                    if x[0] == 1:
                        print("Account No. Verified.")
                        if y[0] == 1:
                            print("Mobile No. Verified.")
                            wd = int(input("Enter Amount To Be Withdrawn:"))
                            mycursor.execute(
                                "select balance from bank_master where acno='"
                                + acno
                                + "'"
                            )
                            a = mycursor.fetchall()
                            for x in a:
                                if x[0] + 30 >= wd:
                                    today = date.today()
                                    dot = str(today.strftime("%y/%m/%d"))
                                    ttype = "w"
                                    mycursor.execute(
                                        "insert into banktrans values('"
                                        + acno
                                        + "','"
                                        + str(wd)
                                        + "','"
                                        + dot
                                        + "','"
                                        + ttype
                                        + "')"
                                    )
                                    mycursor.execute(
                                        "update bank_master set balance=balance-'"
                                        + str(wd)
                                        + "' where acno='"
                                        + acno
                                        + "'"
                                    )
                                    mydb.commit()
                                    print(
                                        "You Have Withdrawn",
                                        wd,
                                        "Rupees From",
                                        acno,
                                        "Account\n",
                                    )
                                else:
                                    print(
                                        "You Can't Withdraw From This Amount (Minimum Amount Exceeds)\n"
                                    )
                        else:
                            print("Mobile No. Is Incorrect\n")
                    else:
                        print("Account Dosent Exists\n")

        elif ch == 4:
            acno = str(input("Enter Account Number :"))
            mycursor.execute(
                "select exists(select * from bank_master where acno='" + acno + "')"
            )
            a = mycursor.fetchall()
            for x in a:
                print("Checking Account No...")
                time.sleep(2)
                if x[0] == 1:
                    print("Account No. Verified.\n")
                    mycursor.execute(
                        "select * from bank_master where acno='" + acno + "'"
                    )
                    for i in mycursor:
                        print("\n")
                        print("Account Number           :-                  ", i[0])
                        print("Account Holder Name   :-                  ", i[1])
                        print(
                            "City Name                     :-                  ", i[2]
                        )
                        print("Mobile Number             :-                  ", i[3])
                        print("BALANCE                     :-                 ", i[4])
                        time.sleep(11)
                        print("\n")
                else:
                    print("Account Dosen't Exist")
        elif ch == 5:
            acno = str(input("Enter Account Number From Which Money Have To Transfer:"))
            acno1 = str(
                input("Enter Account Number In Which You Are Transfering Money :")
            )
            mycursor.execute(
                "select exists(select * from bank_master where acno='" + acno + "')"
            )
            a = mycursor.fetchall()
            mycursor.execute(
                "select exists(select * from bank_master where acno='" + acno1 + "')"
            )
            b = mycursor.fetchall()
            for x in a:
                print("Checking Account No....")
                time.sleep(2)
                for y in b:
                    print("Checking Second Account No....")
                    time.sleep(2)
                    if x[0] == 1:
                        if y[0] == 1:
                            print("Both Account Verified\n")
                            dp = int(input("Enter amount to be Transfer:"))
                            today = date.today()
                            dot = str(today.strftime("%y/%m/%d"))
                            ttype = "d"
                            mycursor.execute(
                                "insert into banktrans values('"
                                + acno
                                + "','"
                                + str(dp)
                                + "','"
                                + dot
                                + "','"
                                + ttype
                                + "')"
                            )
                            mycursor.execute(
                                "update bank_master set balance=balance-'"
                                + str(dp)
                                + "' where acno='"
                                + acno
                                + "'"
                            )
                            mycursor.execute(
                                "update bank_master set balance=balance+'"
                                + str(dp)
                                + "' where acno='"
                                + acno1
                                + "'"
                            )
                            mydb.commit()
                            print("Money Has Been Transferd Successully!!!\n")
                        else:
                            print("Reciving Account Dosent Exists\n")
                    else:
                        print(
                            "Account From Which Money Have To Transfer Dosent Exists\n"
                        )
        elif ch == 6:
            if input("Enter The Password To See Accounts  :") == "SDMS-DSH":
                print("Checking password...")
                time.sleep(2)
                print("Correct Password")
                mycursor.execute("select acno, name from bank_master")
                print("Account no. :-            Account Holder")
                print("\n")
                print("_______________________________")
                for i in mycursor:
                    for j in range(0, len(i) - 1):
                        print(i[j], "           :-           ", i[j + 1])
                print("_______________________________")
                print("\n")
                time.sleep(10)
            else:
                print("Checking password...")
                time.sleep(2)
                print("Wrong Password")
                print(
                    "Contact Deepesh At deepesh.025012@kvsrodelhi.in For The Correct Password\n"
                )
        else:
            root2 = Tk()
            root2.geometry("1x1+40+80")
            root2.overrideredirect(True)
            a = messagebox.askyesno("Feedback", "Do you like our project")
            if a == True:
                root2.destroy()
                print("Thanks")
            else:
                root2.destroy()
                b = input("Enter Here What Can Be Improved:- ")
                time.sleep(2)
                print("Well Tuned, I Will Check That")
                date = date.today()
                file = open("FEEDBACKS\Feedback " + str(date) + ".txt", "a")
                file.write(b + "\n")
                file.close()
            break


def conn1():
    root.after(100, load)
    root.after(5000, conn)


b = Button(root, image=btn, command=conn1, borderwidth=0, bg="black")
b.pack(side=BOTTOM, anchor=CENTER)

root.mainloop()
