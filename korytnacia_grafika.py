import turtle
import random

t = turtle.Turtle()
p = turtle.Turtle()


def stvorec(dlzka):
    for i in range(4):
        t.forward(dlzka)
        p.forward(dlzka)
        t.right(90)
        p.right(90)


def trojuholnik(dlzka):
    for i in range(3):
        t.forward(dlzka)
        p.forward(dlzka)
        t.right(120)
        p.right(120)


def dom(d):
    t.pencolor('blue')
    p.pencolor('blue')
    t.fillcolor('green')
    p.fillcolor('green')
    t.begin_fill()
    p.begin_fill()
    stvorec(d)
    t.end_fill()
    p.end_fill()
    t.lt(60)
    p.lt(60)
    t.pencolor('red')
    p.pencolor('red')
    t.fillcolor('pink')
    p.fillcolor('pink')
    t.begin_fill()
    p.begin_fill()
    trojuholnik(d)
    t.end_fill()
    p.end_fill()
    t.rt(60)
    p.rt(60)


def posun():
    t.pu()
    p.pu()
    t.setpos(random.randint(-100, 100), random.randint(-100, 100))
    p.setpos(random.randint(-100, 100), random.randint(-100, 100))
    t.seth(random.randint(0, 359))
    p.seth(random.randint(0, 359))
    t.pd()
    p.pd()


turtle.delay(5)

for i in range(10):
    t.pensize(random.randint(1,10))
    posun()
    dom(50)
