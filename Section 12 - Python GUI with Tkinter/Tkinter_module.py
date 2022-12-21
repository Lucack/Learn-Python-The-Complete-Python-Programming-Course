from tkinter import *

root = Tk()

    # text in tkinter:
theLabel = Label(root, text = "This is our Tkinter window") # need .pack in variable
theLabel.pack() # pack into the window

    # text in tkinter:
theLabell = Label(root, text = "This is our second sentence") # need .pack in variable
theLabell.pack()

root.mainloop()