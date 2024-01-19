import turtle
import random

col = ["red", "blue", "yellow", "green", "orange", "pink", "purple", "grey", "black"]

t = turtle.Turtle()
a = True
t.pensize(4)

while a is True:
    for i in range(3, 300, 3):
        t.pencolor(random.choice(col))
        t.forward(i)
        t.rt(90)
    a = False

