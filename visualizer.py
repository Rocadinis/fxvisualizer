# (C) Rodrigo Dinis, Gabriel Bonavoluntá, 2023
from turtle import *
import numpy as np
from time import sleep
from tkinter import messagebox
# Grid Setup
title("f(x)Visualizer")
screensize(canvheight=800, canvwidth=800, bg="black")
color("white")
ht()
speed(8)
goto(-800, 0)
forward(1600)
penup()
goto(0, 800)
pendown()
down()
right(90)
forward(1600)
# Info and drawing
def checkf():
    function = textinput("Function box", "Insert a function")
    while function != "" and function is not None:
        pass
        # from this part onward, the program will parse and draw the function. do later
    if function == None:
        messagebox.showerror("Error", "Process aborted.")
        sleep(1)
        done()
    else:
        messagebox.showwarning("Warning", "The function cannot be empty.")
        checkf()
checkf() # Start