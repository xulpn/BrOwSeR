import tkinter
from tkinter import filedialog

def fexplore():
    file = None
    try:
        file = filedialog.Tk().withdraw()
        return filedialog.askopenfile(mode='r').name
    except:
        print(f"Cannot find file '{file}'")
        exit()
