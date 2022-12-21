from tkinter import *

root = Tk()

def printName():
    print("Hello there Avinash f1")

button1 = Button(root,text="Click me",command=printName)
button1.pack()


    # orr:
def printName(event):
    print("Hello there Avinash f2")


button1 = Button(root,text="Click me")
button1.bind("<Button-1>",printName)
button1.pack()


root.mainloop()