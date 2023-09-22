import tkinter
import random

# Pocet vertikalnych a diagonalnych riadkov
# a = int(input("Zadaj počet polí: "))
a = 5

s_p = 500 / a 
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

# Ukladanie súradníc pravého a lavého do listu 
r_sur = []
l_sur = []

# Pole
for v in range(1, a + 1):
    canvas.create_line(s_p * v, 0, s_p * v, 500, width= 5)
    canvas.create_line(0, s_p * v, 500, s_p * v, width= 5)

# Action button
def klik_l(a):
    x = a.x
    y = a.y
    
    print("X-L", x)
    print("Y-L", y)
    print("#######")   
    
    #Súradnica x celočíselné delenie krát šírka pola pre x1, Súradnica y celočíselné delenie krát šírka pola delenie pre y1 
    #Súradnica x celočíselné delenie krát šírka pola plus šírka pola pre x2, Súradnica y celočíselné delenie krát šírka pola plus šírka pola pre y2
    
    canvas.create_oval(x // s_p * s_p, y // s_p * s_p,  x // s_p * s_p + s_p, y // s_p * s_p + s_p, fill="red")

# Action button
def klik_r(b):
    x = b.x
    y = b.y

    print("X-R", x)
    print("Y-R", y)
    print("#######")
    canvas.create_oval(x // s_p * s_p, y // s_p * s_p,  x // s_p * s_p + s_p, y // s_p * s_p + s_p, fill="blue")



canvas.bind("<Button-1>" , klik_l)
canvas.bind("<Button-3>" , klik_r)



tkinter.mainloop()
