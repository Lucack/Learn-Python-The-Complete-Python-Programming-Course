from tkinter import *
import random
import time

def game(event):

    global tk
    global canvas
    global count
    global record
    global startGame
    global toMenu
    global points
    global restart
    global menuevent
    
    canvas.delete("all")
    # canvas = Canvas(tk,width=500,height=500, bd=0 , highlightbackground='white')
    # canvas.pack()
    points = 0

    class Ball:

        def __init__(self,canvas,paddle,color):
            self.canvas=canvas
            self.id = canvas.create_oval(10,10,25,25,fill=color)
            self.canvas.move(self.id,245,100)
                #bounce back:
            start = [-3,-2,1,-1,2,3]
            random.shuffle(start)
            self.x = start[0]
            self.y = -3
            self.canvas_height = 500
            self.canvas_width = 500
            self.paddle = paddle
            self.hit_bottom = False

        def hit_paddle(self, pos):
            global points
            paddle_pos = self.canvas.coords(self.paddle.id)
            if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                    points = points+1
                    return True
                return False

        def draw(self):
            global points
            global record
            self.canvas.move(self.id,self.x,self.y)
            pos = self.canvas.coords(self.id)
            if pos[1] <= 0:
                self.y = 3
            if pos[3] >= 500:
                self.hit_bottom = True
                canvas.create_text(245,100,text="Game Over!",font=("Comic Sans MS",30), fill ='Black')
                score = 'Your Score: ' + str(points)
                record.append(points)
                recordText= 'Your Record: ' + str(max(record))
                canvas.create_text(245,150, text = score, font = ("Comic Sans MS",20) , fill = 'Black') 
                canvas.create_text(245,490, text = recordText, font = ("Comic Sans MS",10) , fill = 'Black') 
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
    ball = Ball(canvas,paddle,'Black')

    
    while True:

        if ball.hit_bottom==True:
            count += 1
            if count == 1:
                startGame.destroy()
                restartGame = Button(None , text="Restart Game",fg="Black")
                restartGame.pack(side=BOTTOM)
            try:
                restartGame.bind("<Button-1>", restartFunction)
            except:
                None   
            if restart == False or menuevent == True:
                toMenu = Button(None , text="Game Menu",fg="Black")
                toMenu.pack(side=BOTTOM)                
            toMenu.bind("<Button-1>", backMenu)
            tk.update()
            menuevent = False      
            break
        else:          
            ball.draw()
            tk.update_idletasks()
            tk.update()
            paddle.draw()
            time.sleep(0.01)
        
    return points, menu

def menu(event):

    global tk
    global canvas
    global count
    global record
    global startGame
    global toMenu
    global points
    global menuevent


    if count == 0:
        tk=Tk()    
        tk.title("Bounce!")
        tk.resizable(0,0)
        tk.wm_attributes("-topmost",1) # in front of all the window
        canvas = Canvas(tk,width=500,height=500, bd=0 , highlightbackground='white')
        canvas.pack() 
    
    if count > 0:
        canvas.delete("all")
        toMenu.destroy()      

    canvas.create_text(245,100,text="Welcome to the Bounce Game!",font=("Comic Sans MS",20), fill ='Black',tags="welcome") 
    canvas.create_text(245,120,text="Bem vindo ao Bounce Game!",font=("Comic Sans MS",20), fill ='Black',tags="bemvindo")
    canvas.pack()  
    time.sleep(1)
    
    record = []     

    if count == 0:
        
        startGame = Button(None , text="Start Game",fg="Black")
        startGame.pack(side=BOTTOM)
        startGame.bind("<Button-1>", game)

    tk.mainloop()

def restartFunction(event):
    global restart
    restart =  True
    game(event)

def backMenu(event):
    global menuevent
    menuevent = True
    menu(event)
    
menuevent = False
restart =  False
strt = 0
count=0
menu(strt)