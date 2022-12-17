import turtle
import time

t = turtle.Pen()
t.color(1,0,1)
for i in range(0,19):
    t.forward(100)
    t.left(95)
time.sleep(1)

    # .up() or .down()
t.up()


t.forward(-180)

t.down()
t.color(0,0,1)
for i in range(0,19):
    t.forward(100)
    t.left(95)
time.sleep(1)

t.color(0,1,0)
t.up()
t.right(90)
t.forward(70)
t.left(90)
t.forward(60)
t.down()

for i in range(0,2):
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.left(90)
time.sleep(4)


