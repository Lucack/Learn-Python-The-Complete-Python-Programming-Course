from tkinter import *

root = Tk()

    # top frame
topFrame = Frame(root)
topFrame.pack(side=TOP)

    # bottom frame
botFrame = Frame(root)
botFrame.pack(side=BOTTOM)



    # Add Button
Button1 = Button(topFrame , text="Button1!",fg="Black")
Button1.pack(side=LEFT)

    # Add second Button
Button2 = Button(topFrame , text="Button2!",fg="Red")
Button2.pack(side=RIGHT)

    # Add 3º Button
Button3 = Button(botFrame , text="Button3!",fg="Orange")
Button3.pack(side=LEFT)

    # Add 4º Button
Button4 = Button(botFrame , text="Button4!",fg="Cyan")
Button4.pack(side=RIGHT)



root.mainloop()