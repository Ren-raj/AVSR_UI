from Tkinter import *
from noise import noise_reducer
import tkMessageBox
import cv2
from  window_view_files import  window_view_file

global screen

def noisered():

    noise_reducer()
    tkMessageBox.showinfo(title=" Noise Reduction ", message= " Noise Reduction Successfull ")
    global screen
    screen.insert(INSERT, "\nclean audio saved as  clean_appaudio.wav\n")

    return

def vidtoframe():
    vidcap = cv2.VideoCapture('appvideo.mp4')
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("/home/ash/Desktop/heart/frames/frame%d.jpg" % count, image)  # save frame as JPEG file
        success, image = vidcap.read()
        screen.insert(END,'Read Frame: %d\n' % count)
        screen.see(END)
        count += 1

    return


def open_window_process():

    process= Toplevel()

    process.geometry("500x550")  # You want the size of the app to be 500x500
    process.resizable(0, 0)
    process.title("AVSR PRE-PROCESSING")

    MainFrame = Frame(process, bg="#08f2c4", padx=40, pady=60)
    MainFrame.pack(fill="both", expand=True)




    button_noisereduction = Button(MainFrame, text="NOISE REDUCTION", font="times 20", padx=40, pady=20, bg="#0bab8c", command=noisered)
    button_noisereduction.pack(fill="x")
    button_vidtfra = Button(MainFrame, text="VIDEO TO FRAME", font="times 20", padx=40, pady=20, bg="#0bab8c", command=vidtoframe)
    button_vidtfra.pack(fill="x", pady=10)

    button_view_file = Button(MainFrame, text="VIEW FILES", font="times 20", padx=60, pady=20, bg="#0bab8c",command=window_view_file)
    button_view_file.pack()

    global screen
    screen=Text(MainFrame, width=60, bg="#67c6a1")
    screen.pack()

    process.mainloop()
    return
