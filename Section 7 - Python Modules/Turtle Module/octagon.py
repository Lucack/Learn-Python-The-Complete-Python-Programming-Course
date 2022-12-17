import turtle
import time
t = turtle.Pen()


n=360/8

for i in range(0,8):
    time.sleep(0.1)
    t.forward(50)
    t.left(n)

t.reset()
time.sleep(1)