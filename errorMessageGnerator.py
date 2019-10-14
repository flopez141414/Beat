import tkinter
from tkinter import messagebox

# hide main window
root = tkinter.Tk()
root.withdraw()

def errorMsgDisplay(message):
    messagebox.showerror("Error", message)

def warningMsgDisplay(message):
    messagebox.showerror("Warning", message)

def infoMsgDisplay(message):
    messagebox.showerror("Information", message)

#errorMsgDisplay("test")