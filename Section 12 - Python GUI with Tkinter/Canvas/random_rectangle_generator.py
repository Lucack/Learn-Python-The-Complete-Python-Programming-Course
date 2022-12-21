from tkinter import *
import random
root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack() 

def randomRec(num):
    for i in range(0,num):
        x1=random.randrange(150)
        x2= x1 + random.randrange(150)
        y1=random.randrange(150)
        y2= y1 +random.randrange(150)
        colors = ["Black", "Red","Pink","Magenta","Blue","Orange","Green","Yellow"]
        canvas.create_rectangle(x1,y1,x2,y2,fill=random.choice(colors))

randomRec(7)
root.mainloop()