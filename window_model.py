from tkinter import *
global screen
from window_featureextraction import open_window_fe
from perform_avsr import  perform_avsr


def openfeatureextraction():

    open_window_fe()

    return


def avsr():

    digit = perform_avsr()
    global screen
    screen.insert(INSERT, str(digit))


    return



def open_window_model():

    model=Toplevel()

    model.geometry("500x550")
    model.resizable(0, 0)
    model.title("Audio Visual Speech Recognition")

    MainFrame = Frame(model, bg="#08f2c4", padx=40, pady=60)
    MainFrame.pack(fill="both", expand=True)

    button_feature_extraction = Button(MainFrame, text="FEATURE EXTRACTION", font="times 20", padx=40, pady=20, bg="#0bab8c", command=openfeatureextraction)
    button_feature_extraction.pack(fill="x")

    button_recognise = Button(MainFrame, text="RECOGNISE", font="times 20", padx=40, pady=20, bg="#0bab8c",command=avsr)
    button_recognise.pack(fill="x", pady=10)

    global screen
    screen = Text(MainFrame, width=60, bg="#67c6a1")
    screen.pack()

    model.mainloop()
    return