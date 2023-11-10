# zadanie z viemeprogramovat(alebo vieme inf) na rekurziu

import turtle

t = turtle.Turtle()

def stvorec_rek(n):
    # for i in range(4):
    t.forward(100/2**(n-1))
    t.left(90)
    if n > 3:
        stvorec_rek(n+1)
    t.right(180)

    t.forward(100/2**(n-1))
    t.left(90)
    if n > 3:
        stvorec_rek(n+1)
    t.right(180)

    t.forward(100/2**(n-1))
    t.left(90)
    if n > 3:
        stvorec_rek(n+1)
    t.right(180)

    t.forward(100/2**(n-1))
    t.left(90)
    if n > 3:
        stvorec_rek(n+1)
    t.right(180)

stvorec_rek(1)
