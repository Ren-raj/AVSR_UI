from Tkinter import *
from PIL import  ImageTk,Image

def open_window_about_us():

    window_about_us = Toplevel()
    window_about_us.title("about us")
    canvas = Canvas(window_about_us, width=550, height=610)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open("/home/ash/Desktop/heart/files/saboutus.png"))
    canvas.create_image(20, 20, anchor=NW, image=img)
    window_about_us.mainloop()