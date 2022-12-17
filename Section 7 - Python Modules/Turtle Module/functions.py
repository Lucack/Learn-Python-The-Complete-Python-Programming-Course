import turtle
import time

t = turtle.Pen()

    # square(side)
def square(side):
    for i in range(0,5):
        t.forward(side)
        t.left(90)

square(100)
square(200)
square(500)

    # circle(radius)
def circle(radius):
    t.circle(radius)

circle(100)
circle(200)
circle(300)

time.sleep(2)

