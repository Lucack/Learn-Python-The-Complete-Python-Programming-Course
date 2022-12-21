from tkinter import *

root = Tk()

label1 = Label(root,text="Label1")
label2 = Label(root,text="Label2")
label3 = Label(root,text="Label3")
label4 = Label(root,text="Label4")

label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=1,column=0)


root.mainloop()