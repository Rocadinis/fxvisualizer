# (C) Rodrigo Dinis, Gabriel Bonavoluntá, 2023
from turtle import *
import numpy as np
from time import sleep
from tkinter import messagebox
# Grid Setup
title("f(x)Visualizer")
screensize(canvheight=800, canvwidth=800, bg="black")
color("white")
speed(3000)
ht()
goto(-800, 0)
for x in range(10):
    forward(70)
    left(90)
    forward(70)
    right(90)
    right(90)
    forward(140)
    left(90)
    left(90)
    forward(70)
    right(90)
forward(140)
for x in range(10):
    forward(70)
    left(90)
    forward(70)
    right(90)
    right(90)
    forward(140)
    left(90)
    left(90)
    forward(70)
    right(90)
penup()
goto(0, 800)
pendown()
down()
right(90)
for x in range(10):
    forward(70)
    left(90)
    forward(70)
    right(90)
    right(90)
    forward(140)
    left(90)
    left(90)
    forward(70)
    right(90)
forward(140)
for x in range(10):
    forward(70)
    left(90)
    forward(70)
    right(90)
    right(90)
    forward(140)
    left(90)
    left(90)
    forward(70)
    right(90)
left(90)
# Info and drawing
def checkf():
    function = textinput("Function box", "Insert a function")
    if function != "" and function is not None: # This is what will calculate and plot the function
        penup()
        color("red")
        left(90)
        pensize(5)
        vals = function.split(",")
        x = vals[0]
        y = vals[1]
        goto (int(x) * 100, int(y) * 100)
        pendown()
        dot(5, "red")
        print(pos())
        #  not completely right, must fix later
        done()
    elif function == None:
        messagebox.showerror("Error", "Process aborted.")
        done()
    else:
        messagebox.showwarning("Warning", "The function cannot be empty.")
        checkf()
checkf() # Start