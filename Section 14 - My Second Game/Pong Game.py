from tkinter import *
import random
import time

class Ball:

    def __init__(self,canvas,color,paddle,paddle1):
        self.canvas = canvas
        self.paddle = paddle
        self.paddle1 = paddle1
        self.id = canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.id, 235,200)
        starts = [-3,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = 500

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                return True
        return False

    def hit_paddle1(self,pos):
        paddle_pos = self.canvas.coords(self.paddle1.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                return True
        return False
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
            self.score(True)
        if pos[2] >= self.canvas_width:
            self.x = -3
            self.score(False)
        if self.hit_paddle(pos) == True:
            self.x = 3
        if self.hit_paddle1(pos) == True:
            self.x = -3

    def score(self, val):
        global point1
        global point2
        if val == True:
            a = self.canvas.create_text(375,40, text = point1, font = ("Arial", 60), fill = "white", tags = "point1")
            canvas.delete('point1') 
            point1 += 1          
            a = self.canvas.create_text(375,40, text = point1, font = ("Arial", 60), fill = "white", tags = "point1")

        if val == False:
            a = self.canvas.create_text(125,40, text = point2, font = ("Arial", 60), fill = "white", tags = "point2")
            canvas.delete('point2')
            point2 += 1
            a = self.canvas.create_text(125,40, text = point2, font = ("Arial", 60), fill = "white", tags = "point2")

class Player1:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,150,30,250, fill = color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('a', self.turn_Down)
        self.canvas.bind_all('s', self.turn_Down)
        self.canvas.bind_all('d', self.turn_Up)
        self.canvas.bind_all('w', self.turn_Up)

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = 0

    def turn_Up(self,evt):
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        else:
            self.y = -3

    def turn_Down(self,evt):
        pos = self.canvas.coords(self.id)
        if pos[3] >= 400:
            self.y = 0
        else:
            self.y = 3

class Player2:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(470,150,500,250, fill =
        color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.y = 0
        self.canvas.bind_all('<KeyPress-Left>', self.turn_Down)
        self.canvas.bind_all('<KeyPress-Down>', self.turn_Down)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_Up)
        self.canvas.bind_all('<KeyPress-Up>', self.turn_Up)

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = 0

    def turn_Down(self,evt):
        pos = self.canvas.coords(self.id)
        if pos[3] >= 400:
            self.y = 0
        else: 
            self.y = 3

    def turn_Up(self,evt):
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        else:
            self.y = -3

def createSpace():
    global tk
    global canvas
    tk = Tk()
    tk.title("Pong")
    tk.resizable(0,0)
    tk.wm_attributes("-topmost",1)
    canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness= 0)
    canvas.pack()
    canvas.config(bg='black')
    canvas.create_line(250,0,250,400,fill="White")
    tk.update()

def createBall(color):
    global ball
    ball = Ball(canvas,color)

# def createPaddle(color):
#     global paddle
#     paddle = Paddle(canvas,color)
    

# def game():
    # while True:
    #     ball.draw()
    #     paddle.draw()
    #     tk.update_idletasks()
    #     tk.update()
    #     time.sleep(0.01) 

        
createSpace()
color='Cyan'
# createBall(color)


player1 = Player1(canvas,"white")
player2 = Player2(canvas,"grey")
point1 = 0
point2 = 0
ball = Ball(canvas,color,player1,player2)

# game()
while True:
    ball.draw()
    player1.draw()
    player2.draw()
    if point1 == 10:
        ball.x = 0
        ball.y = 0
        player1.y = 0
        player2.y = 0
        canvas.create_text(250,200, text = "Congrats Player 2! You Win!", font = 32, fill = "red")
        canvas.create_text(250,215, text = "Score: " + str(point1) + " - " + str(point2), font = 32, fill = "red")
        canvas.pack()
    if point2 == 10:
        ball.x = 0
        ball.y = 0
        player1.y = 0
        player2.y = 0
        canvas.create_text(250,200, text = "Congrats Player 1! You Win!", font = 32, fill = "red")
        canvas.create_text(250,215, text = "Score: " + str(point2) + " - " + str(point1), font = 32, fill = "red")
        canvas.pack()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01) 
    if point1 == 10 or point2 == 10:
        time.sleep(4)