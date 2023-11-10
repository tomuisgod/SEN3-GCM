## viemeprogramovat.sk rekurzia priklad

import turtle

t = turtle.Turtle()

def rek(n, d):
    for i in range(6):        
        t.forward(d)
        if n > 0:

            rek(n-1, d/2.5)
        t.back(d)
        t.right(360/6)
    
rek(1, 100)
