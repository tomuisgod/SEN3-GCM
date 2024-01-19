import turtle

t = turtle.Turtle()


def n_uholnik(n, d):
    for i in range(n):
        t.forward(d)
        t.left(360 / n)


for i in range(3, 16):
    t.clear()
    n_uholnik(i, 50)
