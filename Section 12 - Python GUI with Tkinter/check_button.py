from tkinter import *

root = Tk()

label1 = Label(root,text="Name")
label1.grid(row=0,column=0, sticky="E")

label2 = Label(root, text="Password: ")
label2.grid(row=2,column=0, sticky="E")

entryName = Entry(root)
entryName.grid(row=0,column=1)

entryPass = Entry(root)
entryPass.grid(row=2,column=1)

cbutton = Checkbutton(root, text="Remember login")
# cbutton.grid(row=1,column=1)
cbutton.grid(columnspan=3)


root.mainloop()