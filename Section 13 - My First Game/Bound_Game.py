from tkinter import *
import random
import time

tk = Tk()
tk.title("Bounce!")
tk.resizable(0,0)

tk.wm_attributes("-topmost",1) # in front of all the window

canvas = Canvas(tk,width=500,height=500, bd=0 , highlightbackground='white')
canvas.pack()

class Ball:

    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
            #bounce back:
        start = [-3,-2,-1,0,1,2,3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = 500
        self.canvas_width = 500
        self.paddle = paddle
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= 500:
            self.hit_bottom = True
            canvas.create_text(245,100,text="Game Over!",font=("Comic Sans MS",30), fill ='Black') 
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= 500:
            self.x = -3
        if self.hit_paddle(pos)==True:
            self.y = -3


class Paddles:

    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = 500
        self.canvas.bind_all('<KeyPress-Left>',self.turn_Left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_Right)
        self.canvas.bind_all('<a>',self.turn_Left)
        self.canvas.bind_all('<d>',self.turn_Right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x = 2
        if pos[2]>=500:
            self.x = -2

    def turn_Left(self,evt):
        self.x = -2

    def turn_Right(self,evt):
        self.x = 2
        
paddle = Paddles(canvas,"Cyan")
ball = Ball(canvas,paddle,'Red')

while True:
    if ball.hit_bottom==True:
        time.sleep(2.2)
        break
    ball.draw()
    tk.update_idletasks()
    tk.update()
    paddle.draw()
    time.sleep(0.01)
