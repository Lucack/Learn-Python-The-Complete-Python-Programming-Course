from tkinter import *
root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()   # Now we can add objects in module canvas!!

    # canvas.create.________

# Rectangle
canvas.create_rectangle(20,20,100,270)

canvas.create_line(0,0,300,300)

canvas.create_polygon(0,0,0,200,100,200,100,150,50,150,50,0)
root.mainloop()