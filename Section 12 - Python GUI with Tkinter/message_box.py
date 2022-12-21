from tkinter import *
import tkinter.messagebox
root = Tk()

tkinter.messagebox.showinfo("Message","Did you know that the World just biew up?")

answer = tkinter.messagebox.askquestion("Question 1","Are you human?")

if answer == "yes":
    tkinter.messagebox.showinfo("Congrats","Thank god! Its goot to know another humin is out there")
elif answer == "no":
    tkinter.messagebox.showinfo("Alien","You're a 100% confirmed Alien")


root.mainloop()