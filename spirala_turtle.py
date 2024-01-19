import turtle
import random

col = ["red", "blue", "yellow", "green", "orange", "pink", "purple", "grey", "black"]

t = turtle.Turtle()

def spirala_stvorec():

    t.pensize(4)
    a = True

    while a is True:
        for i in range(3, 300, 3):
            t.pencolor(random.choice(col))
            t.forward(i)
            t.rt(90)
        a = False


def divna_spirala():
    turtle.delay(0)
    for uhol in range(1, 2000):
        t.forward(8)
        t.right(uhol + 0.1)


divna_spirala()

spirala_stvorec()

