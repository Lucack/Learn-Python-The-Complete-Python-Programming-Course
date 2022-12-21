from tkinter import *
import tkinter.messagebox
root = Tk()

equa = ""


equation = StringVar()
calculation = Label(root, textvariable= equation)
equation.set("Enter your equation")
calculation.grid(columnspan = 4)


    # Buttons Calculator

def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)


def equalPress():
    global equa
    total = str(eval(equa))
    equation.set(total)
    equa = total

def clear():
    global equa
    equa = ""
    equation.set("Enter your equation")
# lambda function is a anonymous function

Button1 = Button(root, text="1", command = lambda:btnPress(1))
Button1.grid(row=1,column=0)
Button2 = Button(root, text="2", command = lambda:btnPress(2))
Button2.grid(row=1,column=1)
Button3 = Button(root, text="3", command = lambda:btnPress(3))
Button3.grid(row=1,column=2)
Button4 = Button(root, text="4", command = lambda:btnPress(4))
Button4.grid(row=2,column=0)
Button5 = Button(root, text="5", command = lambda:btnPress(5))
Button5.grid(row=2,column=1)
Button6 = Button(root, text="6", command = lambda:btnPress(6))
Button6.grid(row=2,column=2)
Button7 = Button(root, text="7", command = lambda:btnPress(7))
Button7.grid(row=3,column=0)
Button8 = Button(root, text="8", command = lambda:btnPress(8))
Button8.grid(row=3,column=1)
Button9 = Button(root, text="9", command = lambda:btnPress(9))
Button9.grid(row=3,column=2)
Button0 = Button(root, text="0", command = lambda:btnPress(0)) 
Button0.grid(row=4,column=1)

# Buttonp = Button(root, text=".", command = lambda:btnPress('.')) 
# Buttonp.grid(row=4,column=2)

Plus =Button(root, text="+", command = lambda:btnPress('+')) 
Plus.grid(row=1,column=4)
Minus =Button(root, text="-", command = lambda:btnPress('-')) 
Minus.grid(row=2,column=4)
Multiply =Button(root, text="*", command = lambda:btnPress('*')) 
Multiply.grid(row=3,column=4)
Divide =Button(root, text="/", command = lambda:btnPress('/')) 
Divide.grid(row=4,column=4)

Equal = Button(root, text="=",command = equalPress) 
Equal.grid(row=4,column=2)
Clear = Button(root, text="C", command = clear) 
Clear.grid(row=4,column=0)






root.mainloop()