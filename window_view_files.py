from Tkinter import *
import tkFileDialog
import tkMessageBox
from playsound import playsound
from image_viewer import  photo_view
global view_file

def playclean():

    playsound("clean_appaudio.wav")
    return

def viewf():
    global view_file
    #view_file.withdraw()
    tkMessageBox.showinfo(title="AVSR_select file", message="select the frame you want to see")

    file_dir = tkFileDialog.askopenfilename(title="AVSR_select the frame",initialdir="/home/ash/Desktop/heart")

    try:
        photo_view(file_dir)
    except:
        tkMessageBox.showinfo(title="Exception !", message="Delay Expected \n Try Again.. :)")
        return
    return

def window_view_file():


    global  view_file
    view_file = Toplevel()

    view_file.geometry("500x550")  # You want the size of the app to be 500x500
    view_file.resizable(0, 0)
    view_file.title("AVSR VIEW FILES")

    MainFrame = Frame(view_file, bg="#08f2c4", padx=40, pady=60)
    MainFrame.pack(fill="both", expand=True)

    button_play_clean_audio = Button(MainFrame, text="PLAY CLEAN AUDIO", font="times 20", padx=40, pady=20, bg="#0bab8c",command=playclean)
    button_play_clean_audio.pack(fill="x")

    button_view_frames = Button(MainFrame, text="VIEW  FRAMES", font="times 20", padx=40, pady=20, bg="#0bab8c",command=viewf)
    button_view_frames.pack(fill="x", pady=10)




    view_file.mainloop()
    return

