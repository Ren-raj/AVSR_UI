from tkinter import *

def bar(root, progress, sec):
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(sec)

    progress['value'] = 40
    root.update_idletasks()
    time.sleep(sec)

    progress['value'] = 50
    root.update_idletasks()
    time.sleep(sec)

    progress['value'] = 60
    root.update_idletasks()
    time.sleep(sec)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(sec)
    progress['value'] = 100


    return






# infinite loop
