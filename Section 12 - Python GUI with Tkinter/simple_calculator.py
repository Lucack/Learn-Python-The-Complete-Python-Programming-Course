from tkinter import *
root = Tk()

Label1 = Label(root, text="Enter your expression:")
Label1.pack()

def evaluate(event):
    data = e.get()
    ans.configure(text="Answer: "+ str(eval(data)))


e = Entry(root)
e.bind("<Return>",evaluate)
e.pack()

ans = Label(root)
ans.pack()



root.mainloop()