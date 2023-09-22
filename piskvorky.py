import tkinter
import random

# Pocet vertikalnych a diagonalnych riadkov
# a = int(input("Zadaj počet polí: "))
a = 5

s_p = 500 / a 
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()
 


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
    canvas.create_oval(x // s_p * s_p, y // s_p * s_p,  x // s_p * s_p + s_p, y // s_p * s_p + s_p, fill="red")

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
