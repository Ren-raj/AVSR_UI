from tkinter import *
from tkinter import ttk
global combo
global screen
from audio_feature_extraction import  audio_feature_extraction
from video_feature_extraction import videp_feature_extraction



def audio_features():

    global screen
    screen.delete('1.0', END)
    screen.insert(INSERT, "STARTING AUDIO FEATURE EXTRACTION..\n")
    check = audio_feature_extraction()
    if check:
        screen.insert(END, "AUDIO FEATURE EXTRACTION COMPLETED..\nFILE SAVED  as feature_audio.xlsx..\n")
    else:
        screen.insert(END, "AUDIO FEATURE EXTRACTION FAILED , KINDLY CHECK MODULE ..\n")

    return

def video_features():

    global screen
    screen.delete('1.0', END)
    screen.insert(INSERT, "\nSTARTING VIDEO FEATURE EXTRACTION\n")
    videp_feature_extraction(screen, END)



    return

def check():

    if combo.current()==0:
        audio_features()

    if combo.current()==1:
        video_features()

    return






def open_window_fe():

    windowfe = Tk()

    windowfe.geometry("500x550")
    windowfe.resizable(0, 0)
    windowfe.title("Audio Visual Speech Recognition")


    MainFrame = Frame(windowfe, bg="#08f2c4", padx=40, pady=60 )
    MainFrame.pack(fill="both", expand=True)

    text=Label(MainFrame, text="Select Option -", font="times 20", padx=10, pady=5, bg="#08f2c4")
    text.pack()

    global combo
    combo= ttk.Combobox(MainFrame, values=[" AUDIO FEATURE EXTRACTION  ", " VIDEO FEATURE EXTRACTION "], width=100)
    combo.pack()

    button_proceed = Button(MainFrame, text="PROCEED", font="times 20", padx=40, pady=20, bg="#0bab8c",command=check)
    button_proceed.pack(fill="x", pady=10)

    global screen
    screen = Text(MainFrame, width=60, bg="#67c6a1")
    screen.pack()

    windowfe.mainloop()

    return
