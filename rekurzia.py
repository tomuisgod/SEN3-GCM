import turtle

def strom(n, d):
    forward(d)
    left(45)
    if n > 0:
        strom(n-1, d/2)
        right(90)
        strom(n-1, d/2)
        left(90)
    right(45)
    back(d)

strom(5, 200)
