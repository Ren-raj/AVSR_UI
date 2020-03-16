from Tkinter import *
from window_record import open_window_record
from window_about import  open_window_about
from window_process import open_window_process
from about_us import open_window_about_us
from window_model import  open_window_model
import tkFileDialog


def model():

    open_window_model()

    return

def record():

    open_window_record()

def process():

    open_window_process()

    return

root=Tk()
global i
root.geometry("500x550")
root.resizable(0, 0)
root.title("Audio Visual Speech Recognition")



MainFrame = Frame(root, bg="#08f2c4", padx=40, pady=60 )
MainFrame.pack(fill="both", expand=True)

Heading=Label(MainFrame, text="Audio Visual Speech Recognition",bg="#08f2c4",font="Cooper" ,padx=10, pady=10)
Heading.pack()

Frame1=Frame(MainFrame, bg="#08f2c4")


button_record=Button(Frame1, text="RECORDER",font="times 20", padx=40, pady=20,bg="#0bab8c",command=record)
button_record.pack(fill="x", pady=20)
button_process=Button(Frame1, text="PRE-PROCESS",font="times 20", padx=40, pady=20,bg="#0bab8c", command=process)
button_process.pack(fill="x", pady=20)
button_recognise= Button(Frame1,text="MODEL",font="times 20", padx=40,pady=20,bg="#0bab8c",command=model)
button_recognise.pack(fill="x", pady=20)

Frame1.pack(fill="x")


Frame2=Frame(root)

button_US=Button(Frame2, text="ABOUT US", command=open_window_about_us,padx=15, pady=10)
button_about=Button(Frame2, text="ABOUT AVSR", command=open_window_about,padx=10, pady=10)
button_quit=Button(Frame2, text="EXIT", command=lambda:root.quit(), padx=10, pady=10)


button_US.grid(row=0,column=0, padx=1)
button_about.grid(row=0, column=1, padx=3, pady=0)
button_quit.grid(row=0,column=2,padx=100, pady=0)


Frame2.grid_columnconfigure(0,weight=1)
Frame2.grid_columnconfigure(1,weight=1)
Frame2.grid_columnconfigure(8,weight=1)



Frame2.pack()

root.mainloop()