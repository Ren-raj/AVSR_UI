from moviepy.editor import *
import time
from Tkinter import *
from threading import Thread
import tkMessageBox
import cv2
import sounddevice as sd
from playsound import playsound
from scipy.io.wavfile import write
#from splash import  qt

global E1
global window_record

def func2():

    fs = 44100
    seconds = 4

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    write('appaudio.wav', fs, myrecording)

    return

def func1():

    capture_duration = 3.10

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 40)

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Define the codec and create VideoWriter object
    out = cv2.VideoWriter("appvideo.mp4", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 40, (frame_width, frame_height))

    start_time = time.time()
    while float(time.time() - start_time) < capture_duration:
        ret, frame = cap.read()
        if ret:

            out.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    return

def record():

        #qt()

        t1 = Thread(target=func1)
        t2 = Thread(target=func2)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        global E1
        E1.insert(0, " RECORDING COMPLETED SUCCESSFULLY")

        tkMessageBox.showinfo(title=" RECORDER ",message=" RECORDING SAVED ")

        return


def playaudio():

    playsound("appaudio.wav")

    return

def playvideo():

    os.system("ffplay  -autoexit " + "appvideo.mp4")
    return

def open_window_record():

    global  window_record
    window_record = Toplevel()
    window_record.geometry("500x550")  # You want the size of the app to be 500x500
    window_record.resizable(0, 0)
    window_record.configure(bg='#08f2c4')
    window_record.title("AV RECORD")

    frame1=Frame(window_record,  bg="#08f2c4")


    display =  Label(frame1, text="Audio Visual RECORDER", padx=10,  bg="#08f2c4", pady=10,font="Cooper" )
    button_startrecord = Button(frame1, text="START RECORDING", font="times 20", padx=40, pady=20, bg="#0bab8c", command=record)

    display.pack()
    button_startrecord.pack(fill="x", pady=20)

    frame1.pack()
    global E1
    E1 = Entry(window_record, width=40, bg="#4aeeae")
    E1.pack()

    frame2=Frame(window_record,  bg="#08f2c4")

    button_playaudio = Button(frame2, text="PLAY AUDIO", font="times 20", padx=20, pady=20, bg="#0bab8c", command=playaudio)
    button_playvideo = Button(frame2, text="PLAY VIDEO", font="times 20", padx=20, pady=20, bg="#0bab8c", command=playvideo)

    button_playaudio.grid(row=0, column=0, padx=20, pady=40)

    button_playvideo.grid(row=0, column=1, padx=20, pady=40)
    frame2.pack()

    frame3=Frame(window_record, bg="#08f2c4")

    button_back = Button(frame3,text="BACK", font="times 15", padx=10, pady=10, bg="#0bab8c", command=lambda : window_record.destroy())
    button_back.grid(row=1, column=3,pady=70, padx=80)


    frame3.pack()

    window_record.mainloop()

