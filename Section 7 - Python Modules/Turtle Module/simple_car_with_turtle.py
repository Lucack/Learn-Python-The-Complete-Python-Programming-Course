import turtle
import time

t = turtle.Pen()
t.color(1,0,0)
time.sleep(0.1)
t.begin_fill()
t.forward(2*180) # -->
t.left(90)
t.forward(2*40) # ^
t.left(90)
t.forward(2*40) # <
t.right(90)
t.forward(2*40) # ^
t.left(90)
t.forward(2*100) # < top
t.left(90)
t.forward(2*40)
t.right(90)
t.forward(2*40)
t.left(90)
t.forward(2*40)

t.end_fill() #car sctructure

t.up()
t.left(90)
t.forward(2*25)
t.right(90)
t.forward(2*5)
t.color(0,0,0) # black weeels
t.down()
t.begin_fill()
t.circle(2*20)
t.end_fill() # first wheel

t.up()
t.left(90)
t.forward(2*100)
t.right(90)


t.down()
t.begin_fill()
t.circle(2*20)
t.end_fill() # second wheel
time.sleep(2)







