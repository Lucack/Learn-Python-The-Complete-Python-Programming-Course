from tkinter import *
root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack() 

canvas.create_text(150,150,text="This is my first GUI TEXT!", font=("Calibri",20), fill ='Black' )

root.mainloop()