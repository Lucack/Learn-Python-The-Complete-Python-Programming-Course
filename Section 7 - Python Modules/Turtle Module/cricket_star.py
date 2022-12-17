import turtle
import time

t = turtle.Pen()

for i in range(1,6):
    time.sleep(0.1)
    t.forward(130)
    t.left(145)

time.sleep(2)

t.reset

for i in range(1,38):
    t.forward(130)
    t.left(175)


time.sleep(2)   
   