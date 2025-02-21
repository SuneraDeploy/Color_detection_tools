import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

from colorthief import ColorThief
import os

root=Tk()
root.title("Color picker from image")
root.geometry("800x470+100+100")
root.configure(bg="#e4e8eb")
root.resizable(False,False)


#icon
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)
root.mainloop()
