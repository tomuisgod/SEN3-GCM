import turtle

t = turtle.Turtle()

def strom(n, d):
    t.forward(d)
    t.left(45)
    if n > 0:
        strom(n-1, d/2)
        t.right(90)
        strom(n-1, d/2)
        t.left(90)
    t.right(45)
    t.back(d)

strom(5, 200)
