from tkinter import *
import random
import time
from playsound import playsound

class Ball:

    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        global colorsb
        if darkTheme == True:
            colorsb = ["White","Orange","Cyan","Purple","Yellow","Green","Red","Magenta","Blue","Grey","Pink","Turquoise","Lime","Teal","SystemButtonFace","Light green","Light gray","Violet"]
        else:
            colorsb = ["Black","Orange","Cyan","Purple","Yellow","Green","Red","Magenta","Blue","Grey","Pink","Turquoise","Lime","Teal","SystemButtonFace","Light green","Light gray","Violet"]
        if choiceBall == True:
            self.id = canvas.create_oval(10,10,26,26,fill=colorsb[b])
        else:
            self.id = canvas.create_oval(10,10,26,26,fill=color)
        self.canvas.move(self.id,245,100)
            #bounce back:
        start = [-4,-3,-2,1,-1,2,3,4]
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
                
                if darkTheme == True:
                    colorText = 'White'
                else:
                    colorText = 'Black'

                if en == True:
                    canvas.create_text(250,100,text="Game Over!",font=("Comic Sans MS",30),  fill = colorText)
                    score = 'Your Score: ' + str(points)
                    record.append(points)
                    recordText= 'Your Record: ' + str(max(record))
                else:
                    canvas.create_text(250,100,text="Você Perdeu!",font=("Comic Sans MS",30),  fill = colorText)
                    score = 'Sua Pontuação: ' + str(points)
                    record.append(points)
                    recordText= 'Seu Recorde: ' + str(max(record))
            
                canvas.create_text(250,150, text = score, font = ("Comic Sans MS",20) , fill = colorText) 
                canvas.create_text(250,470, text = recordText, font = ("Comic Sans MS",10) , fill = colorText) 
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= 500:
            self.x = -3
        if self.hit_paddle(pos)==True:
            self.y = -3

class BallTest:
    def __init__(self,canvas,color):
        self.canvas=canvas
        global colorsb
        if darkTheme == True:
            colorsb = ["White","Orange","Cyan","Purple","Yellow","Green","Red","Magenta","Blue","Grey","Pink","Turquoise","Lime","Teal","SystemButtonFace","Light green","Light gray","Violet"]
        else:
            colorsb = ["Black","Orange","Cyan","Purple","Yellow","Green","Red","Magenta","Blue","Grey","Pink","Turquoise","Lime","Teal","SystemButtonFace","Light green","Light gray","Violet"]
        if choiceBall == True:
            self.id = canvas.create_oval(10,10,30,30,fill=colorsb[b])
        else:
            self.id = canvas.create_oval(10,10,30,30,fill=color)
        startx = [200,100,150,50,250,300,350,400,450]
        starty = [200,100,150,50,250,300,350,400,450]
        self.canvas.move(self.id,random.choice(startx),random.choice(starty))
        start = [-3,-2,1,-1,2,3]
        self.x = random.choice(start)
        self.y = random.choice(start)
    
    def drawTest(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 3:
            self.y = 3
        if pos[3] >= 497:
            self.y = -3
        if pos[0] <= 3:
            self.x = 3
        if pos[2] >= 497:
            self.x = -3

class Paddles:

        def __init__(self,canvas,color):
            self.canvas = canvas
            if darkTheme == True:
                colorsp = ["Cyan","White","Orange","Purple","Yellow","Green","Red","Magenta","Blue","Grey","Pink","Turquoise","Lime","Teal","SystemButtonFace","Light green","Light gray","Violet"]
            else:
                colorsp = ["Cyan","Black","Orange","Purple","Yellow","Green","Red","Magenta","Blue","Grey","Pink","Turquoise","Lime","Teal","SystemButtonFace","Light green","Light gray","Violet"]

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
    buttonTheme.destroy()
    points = 0
    
    if choicePaddle == True:
        paddle = Paddles(canvas,colorsp[p])
    else:
        paddle = Paddles(canvas,"Cyan")

    if choiceBall == True:
        ball = Ball(canvas,paddle,colorsb[b])
    else:
        if darkTheme == True:
            ball = Ball(canvas,paddle,'White')
        else:
            ball = Ball(canvas,paddle,'Black')

    while True:
        try:
            canvas.keys()
        except:
            break
        if ball.hit_bottom == True:
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
            try:       
                toMenu.bind("<Button-1>", backMenu)
            except:
                None
            tk.update()
            menuevent = False      
            break
        else:        
            ball.draw()
            paddle.draw()
            tk.update_idletasks()
            tk.update()            
            time.sleep(0.01)
    tk.mainloop()        
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
    global press
    global pressStart
    global pressRestart
    global pressLanguage
    global pressPerso
    global pressTheme
    global buttonTheme
    

    press = False
    pressStart = False
    pressRestart = False
    pressLanguage = False
    pressPerso = False
    pressTheme = False

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
    global colorText

    if darkTheme == True:
        colorText = 'White'
    else:
        colorText = 'Black'

    if darkTheme == True:
        canvas.config(bg='black')
    else:
        canvas.config(bg='SystemButtonFace')
        
    
    record = []     
    if menuevent == True or count > 0:
        count=0
        restartGame.destroy()
        if en == True: 
            canvas.create_text(250,100,text="Bounce Game!",font=("Comic Sans MS",20),fill = colorText)
            restartGame = Button(None , text="Restart Game",fg="Black",command=lambda:pressButton(count,1))
            restartGame.place(x=210,y=250)            
        else:
            canvas.create_text(250,130,text="Bounce Game!",font=("Comic Sans MS",20), fill = colorText)
            restartGame = Button(None , text="Reiniciar o Jogo",fg="Black",command=lambda:pressButton(count,1))
            restartGame.place(x=202,y=250)        
    else:
        if en == True:
            canvas.create_text(250,100,text="Welcome to the Bounce Game!",font=("Comic Sans MS",20),fill = colorText)
            startGame = Button(None , text="Start Game",fg="Black",  width=10, height=1,command=lambda:pressButton(count,2))
        else:
            canvas.create_text(250,130,text="Bem vindo ao Bounce Game!",font=("Comic Sans MS",20), fill = colorText)
            startGame = Button(None , text="Iniciar o Jogo",fg="Black",  width=10, height=1,command=lambda:pressButton(count,2))
        startGame.pack(side=BOTTOM)
        startGame.place(x=208,y=250)
        
    if en == True:
        languageButton = Button(None , text="Change Language",fg="Black",command=lambda:pressButton(count,3))
        languageButton.place(x=194,y=290)
        persoButton = Button(None , text=" Personalize ",fg="Black",  width=10, height=1,command=lambda:pressButton(count,4))
        persoButton.place(x=208,y=330)
        buttonTheme = Button(None , text="Change Theme",fg="Black",  width=12, height=1,command=lambda:pressButton(count,"theme"))
        buttonTheme.place(x=201,y=370)
    else:
        languageButton = Button(None , text=" Trocar Idioma ",fg="Black",command=lambda:pressButton(count,3))
        languageButton.place(x=202,y=290)
        persoButton = Button(None , text="Personalizar",fg="Black",  width=10, height=1,command=lambda:pressButton(count,4))
        persoButton.place(x=207,y=330)
        buttonTheme = Button(None , text="Mudar Tema",fg="Black",  width=12, height=1,command=lambda:pressButton(count,"theme"))
        buttonTheme.place(x=199,y=370)
    

    createBallsTest()
    
    while True:
        try:
            canvas.keys()
        except:
            break
        if press == True:
            if menuevent == True or count > 0:
                if pressRestart == True:
                    restartFunction(count)
            if pressStart == True:
                game(count)
            if pressPerso == True:
                persoFunction(count)
            if pressLanguage == True:
                changeLanguage(count)
            if pressTheme == True:
                changeTheme()
        if press == False:
            try:       
                drawBallTest()
            except:
                None
            tk.update_idletasks()
            tk.update()            
            time.sleep(0.01)        
        
def restartFunction(event):
    global restart
    global restartGame
    restartGame.destroy()
    restart =  True
    game(event)

def backMenu(event):
    global menuevent
    menuevent = True
    try:
        menu(event)
    except:
        None

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
    global inperso

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
    canvas.create_text(250,100,text="Welcome to the Bounce Game!",font=("Comic Sans MS",20), fill = "Black")
    canvas.create_text(250,130,text="Bem vindo ao Bounce Game!",font=("Comic Sans MS",20), fill = "Black")

    canvas.create_text(250,280,text="Select Language:",font=("Comic Sans MS",10), fill = "Black")
    canvas.create_text(250,300,text="Selecione o Idioma:",font=("Comic Sans MS",10), fill = "Black")
    
    buttonPtbr = Button(None , text="Português-BR",fg="Black")
    buttonPtbr.place(x=160,y=320)
    buttonEN = Button(None , text=" English-EN  ",fg="Black")
    buttonEN.place(x=255,y=320)
    
    createBallsTest()

    while True:
        try: 
            canvas.keys()
        except:
            global stop
            stop = 1
            break
        try:
            buttonPtbr.bind("<Button-1>", Language.selectPortugues)
        except:
            None
        try:
            buttonEN.bind("<Button-1>", Language.selectEnglish)
        except:
            None
        drawBallTest()

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
    buttonTheme.destroy()

    if menuevent==True:
        restartGame.destroy()
    if en == True:
        canvas.create_text(250,100,text="Reselect the Language:",font=("Comic Sans MS",20), fill = colorText) 
    if pt == True:
        canvas.create_text(250,100,text="Selecione Novamente o Idioma:",font=("Comic Sans MS",20), fill = colorText) 
    en = False
    pt = False

    canvas.create_text(250,280,text="Select Language:",font=("Comic Sans MS",10),  fill = colorText)
    canvas.create_text(250,295,text="Selecione o Idioma:",font=("Comic Sans MS",10),  fill = colorText)
    
    buttonPtbr = Button(None , text="Português-BR",fg="Black")
    buttonPtbr.place(x=150,y=320)
    buttonEN = Button(None , text=" English-EN  ",fg="Black")
    buttonEN.place(x=250,y=320)

    createBallsTest()

    while True:
        try:
            canvas.keys()
        except:
            break
        buttonPtbr.bind("<Button-1>", Language.selectPortugues)
        buttonEN.bind("<Button-1>", Language.selectEnglish)
        drawBallTest()
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
    global press
    global pressBall
    global pressPaddle
    global pressBack


    canvas.delete("all")
    startGame.destroy()
    persoButton.destroy()
    languageButton.destroy()
    buttonTheme.destroy()
    perso = True
    inperso = False
    press = False
    pressBall = False
    pressPaddle = False
    pressBack = False
    if menuevent==True:
        restartGame.destroy()

    if en == True:
        persoTitle = canvas.create_text(250,100,text="Personalize",font=("Comic Sans MS",20),  fill = colorText)

        ballButton = Button(None , text="Ball Color",fg="Black",  width=10, height=1,command=lambda:pressButton(count,"ball"))
        ballButton.place(x=207,y=250)

        paddleButton = Button(None , text="Paddle Color",fg="Black",  width=10, height=1,command=lambda:pressButton(count,"paddle"))
        paddleButton.place(x=207,y=290)

        backButton = Button(None , text="Back",fg="Black",  width=10, height=1,command=lambda:pressButton(count,"back"))
        backButton.place(x=207,y=330)

    else:
        persoTitle  = canvas.create_text(250,100,text="Personalizar",font=("Comic Sans MS",20),  fill = colorText)

        ballButton = Button(None , text="Ball Color",fg="Black",  width=10, height=1,command=lambda:pressButton(count,"ball"))
        ballButton.place(x=207,y=250)

        paddleButton = Button(None , text="Paddle Color",fg="Black",  width=10, height=1,command=lambda:pressButton(count,"paddle"))
        paddleButton.place(x=207,y=290)

        backButton = Button(None , text="Voltar",fg="Black",  width=10, height=1,command=lambda:pressButton(count,"back"))
        backButton.place(x=207,y=330) 

    createBallsTest()
    objpersoFunction = [ballButton,paddleButton,backButton,persoButton]
    
    while True:
        try:
            canvas.keys()
        except:
            break
        if press == True:
            if pressBall == True:
                colorBall(count)
            if pressPaddle == True:
                colorPaddle(count)
            if pressBack ==  True:
                menu(count)
        if press == False:
            try:       
                drawBallTest()
            except:
                None
            tk.update_idletasks()
            tk.update()            
            time.sleep(0.01)
    
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
        ballTitle = canvas.create_text(250,100,text="Change Ball Color",font=("Comic Sans MS",20),  fill = colorText)
    else:
        ballTitle = canvas.create_text(250,100,text="Mudar Cor da Bola",font=("Comic Sans MS",20),  fill = colorText)
    if darkTheme == True:
        colorsb = ["White","Orange","Cyan","Purple","Yellow","Green","Red","Magenta","Blue","Grey","Pink","Turquoise","Lime","Teal","SystemButtonFace","Light green","Light gray","Violet"]
    else:
        colorsb = ["Black","Orange","Cyan","Purple","Yellow","Green","Red","Magenta","Blue","Grey","Pink","Turquoise","Lime","Teal","SystemButtonFace","Light green","Light gray","Violet"]
    
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
        try:
            canvas.keys()
        except:
            break
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
        canvas.create_text(250,100,text="Change Paddle Color",font=("Comic Sans MS",20),  fill = colorText)
    else:
        canvas.create_text(250,100,text="Mudar Cor do Paddle",font=("Comic Sans MS",20),  fill = colorText)
    if darkTheme == True:
        colorsp = ["Cyan","White","Orange","Purple","Yellow","Green","Red","Magenta","Blue","Grey","Pink","Turquoise","Lime","Teal","SystemButtonFace","Light green","Light gray","Violet"]
    else:
        colorsp = ["Cyan","Black","Orange","Purple","Yellow","Green","Red","Magenta","Blue","Grey","Pink","Turquoise","Lime","Teal","SystemButtonFace","Light green","Light gray","Violet"]
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
        try:
            canvas.keys()
        except:
            break
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

    if choosingPaddle == True: 
        canvas.delete("all")
        if en == True:
            canvas.create_text(250,100,text="Change Paddle Color",font=("Comic Sans MS",20),  fill = colorText)
        else:
            canvas.create_text(250,100,text="Mudar Cor do Paddle",font=("Comic Sans MS",20),  fill = colorText)
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
            canvas.create_text(250,100,text="Change Ball Color",font=("Comic Sans MS",20),  fill = colorText)
        else:
            canvas.create_text(250,100,text="Mudar Cor da Bola",font=("Comic Sans MS",20),  fill = colorText)
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
            canvas.create_text(250,100,text="Change Ball Color",font=("Comic Sans MS",20),  fill = colorText)
        else:
            canvas.create_text(250,100,text="Mudar Cor da Bola",font=("Comic Sans MS",20),  fill = colorText)
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
            canvas.create_text(250,100,text="Change Paddle Color",font=("Comic Sans MS",20),  fill = colorText)
        else:
            canvas.create_text(250,100,text="Mudar Cor do Paddle",font=("Comic Sans MS",20),  fill = colorText)
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
            canvas.create_text(250,100,text="Change Ball Color",font=("Comic Sans MS",20),  fill = colorText)
        else:
            canvas.create_text(250,100,text="Mudar Cor da Bola",font=("Comic Sans MS",20),  fill = colorText)
        paddle = Paddles(canvas,colorsp[p])

        tk.update_idletasks()
        tk.update()
        b = b - 1
        if b < 0:
            b = len(colorsb)-1
        ball = Ball(canvas,paddle,colorsb[b])

    else: # choosingBall == True:
        if en == True:
            canvas.create_text(250,100,text="Change Ball Color",font=("Comic Sans MS",20),  fill = colorText)
        else:
            canvas.create_text(250,100,text="Mudar Cor da Bola",font=("Comic Sans MS",20),  fill = colorText)
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

def createBallsTest():    
    if darkTheme == True:
        colorsb = ["White","Orange","Cyan","Purple","Yellow","Green","Red","Magenta","Blue","Grey","Pink","Turquoise","Lime","Teal","SystemButtonFace","Light green","Light gray","Violet"]
    else:
        colorsb = ["Black","Orange","Cyan","Purple","Yellow","Green","Red","Magenta","Blue","Grey","Pink","Turquoise","Lime","Teal","SystemButtonFace","Light green","Light gray","Violet"]
    
    c1 = random.choice(colorsb)
    colorsb.remove(c1)
    global balltest1
    balltest1 = BallTest(canvas,c1)
    c2 = random.choice(colorsb)
    colorsb.remove(c2)
    global balltest2
    balltest2 = BallTest(canvas,c2)
    c3 = random.choice(colorsb)
    colorsb.remove(c3)
    global balltest3
    balltest3 = BallTest(canvas,c3)
    c4 = random.choice(colorsb)
    colorsb.remove(c4)
    global balltest4
    balltest4 = BallTest(canvas,c4)
    c5 = random.choice(colorsb)
    colorsb.remove(c5)
    global balltest5
    balltest5 = BallTest(canvas,c5)
    c6 = random.choice(colorsb)
    colorsb.remove(c6)
    global balltest6
    balltest6 = BallTest(canvas,c6)
    c7 = random.choice(colorsb)
    colorsb.remove(c7)
    global balltest7
    balltest7 = BallTest(canvas,c7)
    c8 = random.choice(colorsb)
    colorsb.remove(c8)
    global balltest8
    balltest8 = BallTest(canvas,c8)
    c9 = random.choice(colorsb)
    colorsb.remove(c9)
    global balltest9
    balltest9 = BallTest(canvas,c9)
    c10 = random.choice(colorsb)
    colorsb.remove(c10)
    global balltest10
    balltest10 = BallTest(canvas,c10)
    c11 = random.choice(colorsb)
    colorsb.remove(c11)
    global balltest11
    balltest11 = BallTest(canvas,c11)
    c12 = random.choice(colorsb)
    colorsb.remove(c12)
    global balltest12
    balltest12 = BallTest(canvas,c12)
    c13 = random.choice(colorsb)
    colorsb.remove(c13)
    global balltest13
    balltest13 = BallTest(canvas,c13)
    c14 = random.choice(colorsb)
    colorsb.remove(c14)
    global balltest14
    balltest14 = BallTest(canvas,c14)
    c15 = random.choice(colorsb)
    colorsb.remove(c15)
    global balltest15
    balltest15 = BallTest(canvas,c15)

def drawBallTest():
    balltest1.drawTest()
    balltest2.drawTest()
    balltest3.drawTest()
    balltest4.drawTest()
    balltest5.drawTest()
    balltest6.drawTest()
    balltest7.drawTest()
    balltest8.drawTest()
    balltest9.drawTest()
    balltest10.drawTest()
    balltest11.drawTest()
    balltest12.drawTest()
    balltest13.drawTest()
    balltest14.drawTest()
    balltest15.drawTest()
    tk.update_idletasks()
    tk.update()

def pressButton(event,button):
    global press
    global pressStart
    global pressRestart
    global pressLanguage
    global pressPerso
    global pressBall
    global pressPaddle
    global pressBack
    global pressTheme

    if button == 1:
        pressRestart = True
    if button == 2:
        pressStart = True
    if button == 3:
        pressLanguage = True
    if button == 4:
        pressPerso = True
    if button == "ball":
        pressBall = True
    if button == "paddle":
        pressPaddle = True
    if button == "back":
        pressBack = True
    if button == "theme":
        pressTheme = True
    press = True

def changeTheme():
    global darkTheme
    if darkTheme == False:
        darkTheme = True
    else:
        darkTheme = False
    canvas.delete("all")
    startGame.destroy()
    languageButton.destroy()
    persoButton.destroy()
    buttonTheme.destroy()

    menu(count)

darkTheme = False
p = 0
choosingPaddle = False
b = 0
choosingBall = False
choiceBall = False
choicePaddle = False
perso = False
inperso = False
stop = 0
intro()
if stop != 1:
    # menu(p)
    try:
        menu(p)
    except:
        None