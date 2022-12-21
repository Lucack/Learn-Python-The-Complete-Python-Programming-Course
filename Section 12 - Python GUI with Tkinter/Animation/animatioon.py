from tkinter import *
import random
import time

root = Tk()
canvas = Canvas(root, width=290, height=290)
canvas.pack() 
y=290
a= 50,y,70,y,70,270,50,270
canvas.create_polygon(a)
canvas.create_line(0,290,300,290)

    # canvas.move( objectID , how many pixel in X , in Y)

def leftClick(event):
    canvas.move(1,-10,0)
    root.update() # update changes
    time.sleep(0.02)

def rightClick(event):
    canvas.move(1,10,0)
    root.update() # update changes
    time.sleep(0.02)

def upClick(event):
    canvas.move(1,0,-10)
    root.update() # update changes
    time.sleep(0.02)

def downClick(event):
    global y
    if y < 290:
        canvas.move(1,0,0)
        root.update() # update changes
    else:
        canvas.move(1,0,10)
        root.update() # update changes
        time.sleep(0.02)

def downClick(event):
    canvas.move(1,0,10)
    root.update() # update changes
    time.sleep(0.02)


root.geometry("700x700")

root.bind("<Left>", leftClick)
root.bind("<Right>", rightClick)
root.bind("<Up>", upClick)
root.bind("<Down>", downClick)




root.mainloop()