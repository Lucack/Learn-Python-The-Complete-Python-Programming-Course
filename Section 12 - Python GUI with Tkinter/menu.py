from tkinter import *
import tkinter.messagebox
root = Tk()

def random():
    print("This is a statement")
def newFile():
    print("This is a newFilee!")

mainMenu = Menu(root)
root.configure(menu = mainMenu)

subMenu = Menu(mainMenu)
mainMenu.add_cascade(label="File",menu=subMenu)

subMenu.add_command(label="Random Func",command=random)
subMenu.add_command(label="New File",command=newFile)
subMenu.add_separator()
subMenu.add_command(label="Supercalafragilistic",command=random)

root.mainloop()