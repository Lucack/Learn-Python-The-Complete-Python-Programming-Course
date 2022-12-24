from tkinter import *
import random
import time
from playsound import playsound

class Ball:

    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        global colorsb
        if choiceBall == True:
            self.id = canvas.create_oval(10,10,25,25,fill=colorsb[b])
        else:
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
                if inperso == False:                        
                    points = points+1
                # hitSound()
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
            if inperso == True:
                self.y = -3
            else:
                self.hit_bottom = True
                if en == True:
                    canvas.create_text(250,100,text="Game Over!",font=("Comic Sans MS",30), fill ='Black')
                    score = 'Your Score: ' + str(points)
                    record.append(points)
                    recordText= 'Your Record: ' + str(max(record))
                else:
                    canvas.create_text(250,100,text="Você Perdeu!",font=("Comic Sans MS",30), fill ='Black')
                    score = 'Sua Pontuação: ' + str(points)
                    record.append(points)
                    recordText= 'Seu Recorde: ' + str(max(record))
            
                canvas.create_text(250,150, text = score, font = ("Comic Sans MS",20) , fill = 'Black') 
                canvas.create_text(250,470, text = recordText, font = ("Comic Sans MS",10) , fill = 'Black') 
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= 500:
            self.x = -3
        if self.hit_paddle(pos)==True:
            self.y = -3

class Paddles:

        def __init__(self,canvas,color):
            self.canvas = canvas
            if choicePaddle == True:
                self.id = canvas.create_rectangle(0,0,100,10,fill=colorsp[p])
            else:
                self.id = canvas.create_rectangle(0,0,100,10,fill=color)
            self.canvas.move(self.id, 200, 350)
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

class Language:
        def __init__(self):
            pass
        def selectPortugues(event):
            global pt
            pt = True          
        def selectEnglish(event):
            global en
            en = True

def game(event):
    global count
    global restartGame
    global toMenu
    global points
    global restart
    global menuevent
    global ball
    global paddle
    
    canvas.delete("all")
    startGame.destroy()
    languageButton.destroy()
    persoButton.destroy()
    points = 0

    if choicePaddle == True:
        paddle = Paddles(canvas,colorsp[p])
    else:
        paddle = Paddles(canvas,"Cyan")

    if choiceBall == True:
        ball = Ball(canvas,paddle,colorsb[b])
    else:
        ball = Ball(canvas,paddle,'Black')

    while True:

        if ball.hit_bottom==True:
            count += 1
            if restart == False or menuevent == True:
                if en == True:
                    toMenu = Button(None , text="Game Menu",fg="Black")
                else:
                    toMenu = Button(None , text="Menu do Jogo",fg="Black")
                toMenu.pack(side=BOTTOM)  

            if count == 1 or menuevent == False:
                startGame.destroy()
                if en == True:
                    restartGame = Button(None , text="Restart Game",fg="Black")
                else:
                    restartGame = Button(None , text="Reiniciar o Jogo",fg="Black")
                restartGame.pack(side=BOTTOM)
            try:
                restartGame.bind("<Button-1>", restartFunction)
            except:
                None       
            toMenu.bind("<Button-1>", backMenu)
            tk.update()
            menuevent = False      
            break
        else:          
            ball.draw()
            paddle.draw()
            tk.update_idletasks()
            tk.update()            
            time.sleep(0.01)
        
    return points, menu

def menu(event):

    global record
    global startGame
    global restartGame
    global toMenu
    global points
    global count
    global languageButton
    global persoButton
    global perso
    
    if perso == True:
        canvas.delete("all")
        for i in objpersoFunction:
            i.destroy()
        perso = False

    if count > 0:
        canvas.delete("all")
        toMenu.destroy()
    
    canvas.pack()  
    time.sleep(0.01)
    
    record = []     
    if menuevent == True or count > 0:
        count=0
        restartGame.destroy()
        if en == True: 
            canvas.create_text(250,100,text="Bounce Game!",font=("Comic Sans MS",20), fill ='Black')
            restartGame = Button(None , text="Restart Game",fg="Black")
            restartGame.place(x=210,y=260)
        else:
            canvas.create_text(250,130,text="Bounce Game!",font=("Comic Sans MS",20), fill ='Black')
            restartGame = Button(None , text="Reiniciar o Jogo",fg="Black")
            restartGame.place(x=202,y=260)
        
        restartGame.bind("<Button-1>", restartFunction)
        
    else:
        if en == True:
            canvas.create_text(250,100,text="Welcome to the Bounce Game!",font=("Comic Sans MS",20), fill ='Black')
            startGame = Button(None , text="Start Game",fg="Black",  width=10, height=1)
        else:
            canvas.create_text(250,130,text="Bem vindo ao Bounce Game!",font=("Comic Sans MS",20), fill ='Black')
            startGame = Button(None , text="Iniciar o Jogo",fg="Black",  width=10, height=1)
        # startGame.pack(side=BOTTOM)
        startGame.place(x=208,y=250)
        
        startGame.bind("<Button-1>", game)
    if en == True:
        languageButton = Button(None , text="Change Language",fg="Black")
        languageButton.place(x=194,y=290)
        persoButton = Button(None , text=" Personalize ",fg="Black",  width=10, height=1)
        persoButton.place(x=208,y=330)
    else:
        languageButton = Button(None , text=" Trocar Idioma ",fg="Black")
        languageButton.place(x=202,y=290)
        persoButton = Button(None , text="Personalizar",fg="Black",  width=10, height=1)
        persoButton.place(x=207,y=330)
    persoButton.bind("<Button-1>", persoFunction)
    languageButton.bind("<Button-1>", changeLanguage)

    tk.mainloop()

def restartFunction(event):
    global restart
    global restartGame
    restartGame.destroy()
    restart =  True
    game(event)

def backMenu(event):
    global menuevent
    menuevent = True
    menu(event)

def hitSound():
    local = 'Jump_sound.wav'
    playsound(local, False)

def intro():

    global tk
    global canvas
    global count
    global menuevent
    global restart
    global en
    global pt

    count = 0
    menuevent = False
    restart =  False
    en = False
    pt = False

    tk=Tk()    
    tk.title("Bounce Game!")
    tk.resizable(0,0)
    tk.wm_attributes("-topmost",1) # in front of all the window
    canvas = Canvas(tk,width=500,height=500, bd=0 , highlightbackground='white')
    canvas.pack()
    canvas.create_text(250,100,text="Welcome to the Bounce Game!",font=("Comic Sans MS",20), fill ='Black') 
    canvas.create_text(250,130,text="Bem vindo ao Bounce Game!",font=("Comic Sans MS",20), fill ='Black')

    canvas.create_text(250,280,text="Select Language:",font=("Comic Sans MS",10), fill ='Black')
    canvas.create_text(250,295,text="Selecione o Idioma:",font=("Comic Sans MS",10), fill ='Black')
    
    buttonPtbr = Button(None , text="Português-BR",fg="Black")
    buttonPtbr.place(x=150,y=320)
    buttonEN = Button(None , text=" English-EN  ",fg="Black")
    buttonEN.place(x=250,y=320)

    while True:
        buttonPtbr.bind("<Button-1>", Language.selectPortugues)
        buttonEN.bind("<Button-1>", Language.selectEnglish)
        if en == True or pt == True:
            intro = 1
            canvas.delete("all")
            buttonPtbr.destroy()
            buttonEN.destroy()
            return intro
        tk.update_idletasks()
        tk.update()            
        time.sleep(0.01)

def changeLanguage(event):

    global en
    global pt
    global languageButton 

    canvas.delete("all")

    startGame.destroy()
    languageButton.destroy()
    persoButton.destroy()

    if menuevent==True:
        restartGame.destroy()
    if en == True:
        canvas.create_text(250,100,text="Reselect the Language:",font=("Comic Sans MS",20), fill ='Black')
    if pt == True:
        canvas.create_text(250,100,text="Selecione Novamente o Idioma:",font=("Comic Sans MS",20), fill ='Black')
    en = False
    pt = False

    canvas.create_text(250,280,text="Select Language:",font=("Comic Sans MS",10), fill ='Black')
    canvas.create_text(250,295,text="Selecione o Idioma:",font=("Comic Sans MS",10), fill ='Black')
    
    buttonPtbr = Button(None , text="Português-BR",fg="Black")
    buttonPtbr.place(x=150,y=320)
    buttonEN = Button(None , text=" English-EN  ",fg="Black")
    buttonEN.place(x=250,y=320)

    while True:
        buttonPtbr.bind("<Button-1>", Language.selectPortugues)
        buttonEN.bind("<Button-1>", Language.selectEnglish)
        if en == True or pt == True:
            canvas.delete("all")
            buttonPtbr.destroy()
            buttonEN.destroy()
            menu(event)
        tk.update_idletasks()
        tk.update()            
        time.sleep(0.01)

def persoFunction(event):

    global persoTitle
    global ballButton
    global paddleButton
    global backButton
    global perso
    global inperso
    global objpersoFunction

    canvas.delete("all")
    startGame.destroy()
    persoButton.destroy()
    languageButton.destroy()
    perso = True
    inperso = False

    if menuevent==True:
        restartGame.destroy()

    if en == True:
        persoTitle = canvas.create_text(250,100,text="Personalize",font=("Comic Sans MS",20), fill ='Black')

        ballButton = Button(None , text="Ball Color",fg="Black",  width=10, height=1)
        ballButton.place(x=207,y=250)

        paddleButton = Button(None , text="Paddle Color",fg="Black",  width=10, height=1)
        paddleButton.place(x=207,y=290)

        backButton = Button(None , text="Back",fg="Black",  width=10, height=1)
        backButton.place(x=207,y=330)

    else:
        persoTitle  = canvas.create_text(250,100,text="Personalizar",font=("Comic Sans MS",20), fill ='Black')

        ballButton = Button(None , text="Ball Color",fg="Black",  width=10, height=1)
        ballButton.place(x=207,y=250)

        paddleButton = Button(None , text="Paddle Color",fg="Black",  width=10, height=1)
        paddleButton.place(x=207,y=290)

        backButton = Button(None , text="Voltar",fg="Black",  width=10, height=1)
        backButton.place(x=207,y=330) 
    
    
    ballButton.bind("<Button-1>", colorBall)  
    paddleButton.bind("<Button-1>", colorPaddle)
    backButton.bind("<Button-1>", menu)  # if perso = True to del
    objpersoFunction = [ballButton,paddleButton,backButton,persoButton]
    
def colorBall(event):

    global b
    global colorsb
    global choiceBall
    global ball
    global paddle
    global objcolorBall
    global ballTitle
    global inperso
    global choosingBall
    global choicePaddle

    inperso = True
    choiceBall = False
    choosingBall = True

    for i in objpersoFunction:
        i.destroy()
    
    canvas.delete("all")
    if en == True:
        ballTitle = canvas.create_text(250,100,text="Change Ball Color",font=("Comic Sans MS",20), fill ='Black')
    else:
        ballTitle = canvas.create_text(250,100,text="Mudar Cor da Bola",font=("Comic Sans MS",20), fill ='Black')
    colorsb = ["Black","Orange","Cyan","Purple","Yellow","Green","Red","Magenta","Blue","Grey","Pink","Turquoise","Lime","Teal"]

    buttonleft = Button(None , text="<-",fg="Black",  width=5, height=2)
    buttonleft.place(x=2,y=250)
    buttonleft.bind("<Button-1>", left)

    buttonright = Button(None , text="->",fg="Black",  width=5, height=2)
    buttonright.place(x=458,y=250)
    buttonright.bind("<Button-1>", right)

    if en == True:
        selectButton = Button(None , text="Select",fg="Black",  width=5, height=2)
        selectButton.place(x=227,y=400)
    else:
        selectButton = Button(None , text="Selecionar",fg="Black",  width=8, height=2)
        selectButton.place(x=215,y=400)
    selectButton.bind("<Button-1>", selectBall) 
    b=0

    if choicePaddle == True:
        paddle = Paddles(canvas,colorsp[p])
    else: 
        paddle = Paddles(canvas,"Cyan")

    ball = Ball(canvas,paddle,colorsb[b])
    objcolorBall = [selectButton,buttonright,buttonleft]

    while choiceBall == False:
        ball.draw()
        tk.update_idletasks()
        tk.update()            
        time.sleep(0.01)

def colorPaddle(event):

    global p
    global colorsp
    global choicePaddle
    global ball
    global paddle
    global objcolorPaddle
    global ballTitle
    global inperso
    global choosingPaddle

    inperso = True
    choosingPaddle = True
    choicePaddle = False

    for i in objpersoFunction:
        i.destroy()
    
    canvas.delete("all")
    if en == True:
        canvas.create_text(250,100,text="Change Paddle Color",font=("Comic Sans MS",20), fill ='Black')
    else:
        canvas.create_text(250,100,text="Mudar Cor do Paddle",font=("Comic Sans MS",20), fill ='Black')
    colorsp = ["Cyan","Black","Orange","Purple","Yellow","Green","Red","Magenta","Blue","Grey","Pink","Turquoise","Lime","Teal"]

    buttonleft = Button(None , text="<-",fg="Black",  width=5, height=2)
    buttonleft.place(x=2,y=250)
    buttonleft.bind("<Button-1>", left)

    buttonright = Button(None , text="->",fg="Black",  width=5, height=2)
    buttonright.place(x=458,y=250)
    buttonright.bind("<Button-1>", right)

    if en == True:
        selectButton = Button(None , text="Select",fg="Black",  width=5, height=2)
        selectButton.place(x=227,y=400)
    else:
        selectButton = Button(None , text="Selecionar",fg="Black",  width=8, height=2)
        selectButton.place(x=215,y=400)
    selectButton.bind("<Button-1>", selectPaddle) 

    paddle = Paddles(canvas,"Cyan")
    if choiceBall == True:
        ball = Ball(canvas,paddle,colorsb[b])
    else: 
        ball = Ball(canvas,paddle,"Black")
    objcolorPaddle = [selectButton,buttonright,buttonleft]

    while choicePaddle == False:
        ball.draw()
        paddle.draw()
        tk.update()  
        tk.update_idletasks()
        tk.update()           
        time.sleep(0.01)

def right(event):

    global ball
    global paddle
    global b
    global p

    canvas.delete("all")

    if choosingPaddle == True: #
        canvas.delete("all")
        if en == True:
            canvas.create_text(250,100,text="Change Paddle Color",font=("Comic Sans MS",20), fill ='Black')
        else:
            canvas.create_text(250,100,text="Mudar Cor do Paddle",font=("Comic Sans MS",20), fill ='Black')
        paddle = Paddles(canvas,colorsp[p])
        if choiceBall == True:
            ball = Ball(canvas,paddle,colorsb[b])
        else: 
            ball = Ball(canvas,paddle,"Black")  
        tk.update_idletasks()
        tk.update()
        p = p + 1
        if p >= len(colorsp):
            p = 0  
        paddle = Paddles(canvas,colorsp[p])
        
    elif choosingBall == True and choicePaddle == True: #
        canvas.delete("all")
        if en == True:
            canvas.create_text(250,100,text="Change Ball Color",font=("Comic Sans MS",20), fill ='Black')
        else:
            canvas.create_text(250,100,text="Mudar Cor da Bola",font=("Comic Sans MS",20), fill ='Black')
        paddle = Paddles(canvas,colorsp[p])
        tk.update_idletasks()
        tk.update()
        b = b + 1
        if b >= len(colorsb):
            b = 0  
        ball = Ball(canvas,paddle,colorsb[b])

    else: # choosingBall == True:

        canvas.delete("all")
        if en == True:
            canvas.create_text(250,100,text="Change Ball Color",font=("Comic Sans MS",20), fill ='Black')
        else:
            canvas.create_text(250,100,text="Mudar Cor da Bola",font=("Comic Sans MS",20), fill ='Black')
        paddle = Paddles(canvas,"Cyan")  
        tk.update_idletasks()
        tk.update()
        
        b = b + 1
        if b >= len(colorsb):
            b = 0  
        ball = Ball(canvas,paddle,colorsb[b])
    
def left(event):
    
    global ball
    global paddle
    global b
    global p

    canvas.delete("all")

    if choosingPaddle == True:
        if en == True:
            canvas.create_text(250,100,text="Change Paddle Color",font=("Comic Sans MS",20), fill ='Black')
        else:
            canvas.create_text(250,100,text="Mudar Cor do Paddle",font=("Comic Sans MS",20), fill ='Black')
        paddle = Paddles(canvas,"Cyan")
        paddle = Paddles(canvas,colorsp[p])
        if choiceBall == True:
            ball = Ball(canvas,paddle,colorsb[b])
        else: 
            ball = Ball(canvas,paddle,"Black")  
        tk.update_idletasks()
        tk.update()
        p = p - 1
        if p < 0:
            p = len(colorsp)-1
        paddle = Paddles(canvas,colorsp[p])  
        
    elif choosingBall == True and choicePaddle == True:
        if en == True:
            canvas.create_text(250,100,text="Change Ball Color",font=("Comic Sans MS",20), fill ='Black')
        else:
            canvas.create_text(250,100,text="Mudar Cor da Bola",font=("Comic Sans MS",20), fill ='Black')
        paddle = Paddles(canvas,colorsp[p])

        tk.update_idletasks()
        tk.update()
        b = b - 1
        if b < 0:
            b = len(colorsb)-1
        ball = Ball(canvas,paddle,colorsb[b])

    else: # choosingBall == True:
        if en == True:
            canvas.create_text(250,100,text="Change Ball Color",font=("Comic Sans MS",20), fill ='Black')
        else:
            canvas.create_text(250,100,text="Mudar Cor da Bola",font=("Comic Sans MS",20), fill ='Black')
        paddle = Paddles(canvas,"Cyan")  

        tk.update_idletasks()
        tk.update()
        b = b - 1
        if b < 0 :
            b = len(colorsb)-1  
        ball = Ball(canvas,paddle,colorsb[b])

def selectBall(event):

    global choiceBall
    global objcolorBall
    global inperso
    global choosingBall
    canvas.delete("all")  
    for i in objcolorBall:
        i.destroy()
    choiceBall = True
    inperso = False
    choosingBall = False
    persoFunction(b)

def selectPaddle(event):

    global choicePaddle
    global objcolorPaddle
    global inperso
    global choosingPaddle
    canvas.delete("all")  
    for i in objcolorPaddle:
        i.destroy()
    choicePaddle = True
    inperso = False
    choosingPaddle = False
    persoFunction(p)

p = 0
choosingPaddle = False
b = 0
choosingBall = False
choiceBall = False
choicePaddle = False
perso = False
inperso = False
start = intro()
menu(start)