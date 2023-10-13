import tkinter
import random

canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()


x = 5
w = 500//x
pole = []
pole.append([-1]*(x+2))
for i in range(x):
    pole.append([-1]+[0]*x)
pole.append([-1]*(x+2))

print(pole)
for i in range(1,x+1):
    canvas.create_line(0, 500/x*i, 500, 500/x*i)
    canvas.create_line(500/x*i, 0, 500/x*i, 500)

pocet_min = 0
while pocet_min <= 10:
    rand_x = random.randrange(len(pole))+1
    rand_y = random.randrange(len(pole))+1

    if pole[rand_x][rand_y] != 9:
        pole[rand_x][rand_y] = 9
        pocet_min += 1

for i in range(1, len(pole)-1):
    for j in range(1, len(pole)-1):
        if pole[i][j] != 9:
            okolite_miny = 0
            for k in range(-1, 2):  
                for l in range(-1,2):
                    if pole[i+k][j+l] == 9:
                        okolite_miny += 1
            pole[i][j] = okolite_miny

def klik(a):
    print("-------")
    print("x",a.x)
    print("y",a.y)
    print("-------")
    print("\n")
    canvas.create_oval(a.x//w*w, a.y//w*w, a.x//w*w+w, a.y//w*w+w)
    pole[a.y//w][a.x//w]=1

canvas.bind("<Button-1>",klik)


canvas.mainloop()
