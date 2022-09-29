from tkinter import *
from PIL import Image, ImageTk
from itertools import count, cycle
import threading as th
from win32api import GetSystemMetrics


'''-------------------------------------'''
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
mid_width = int(width/2)-300
win_width = 100
win_height = 60
#mid_width_block = mid_width+300-
'''-------------------------------------'''
 
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
            self.delay = im.info['duration']
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
 
'''------Main_Gif_Screen-----------------'''
root = Tk()
root.overrideredirect(1)
root.geometry(f'+{mid_width}+165')
lbl = ImageLabel(root)
lbl.pack()
lbl.load('circle.gif')
root.after(5000,lambda: root.destroy())
'''---------------------------------------'''
'''----------Top screen for text----------'''
top = Toplevel()
top.configure(bg="black")
top.overrideredirect(1)
top.geometry("200x40+860+485")
top.lift(root)
frame = LabelFrame(top,padx=40,bg="#181D24",borderwidth=0)
frame.pack()
l=Label(frame,text="Loading...",bg="#181D24",fg="white",font=("harlow solid italic",17)).grid(row=0,column=0)
'''---------------------------------------'''
top.mainloop()
