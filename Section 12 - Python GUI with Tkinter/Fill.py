from tkinter import *

root = Tk()

    # Add Button
Button1 = Button(None , text="Button1!",fg="Black")
Button1.pack()

    # Add second Button
Button2 = Button(None , text="Button2!",fg="Red")
Button2.pack(fill=X)

    # Add 3º Button
Button3 = Button(None , text="Button3!",fg="Orange")
Button3.pack(side=RIGHT,fill=Y)

    # Add 4º Button
Button4 = Button(None , text="Button4!",fg="Cyan")
Button4.pack()



root.mainloop()