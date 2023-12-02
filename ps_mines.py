"""
DISCLAIMER:
NEFUNKCNA VERZIA, UPDATE PRIDE 8.12.2023
"""



import tkinter
import random

canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()


x = 5
w = 500//x
pole = []
pole.append([-1]*(x+2))
for i in range(x):
    pole.append([-1]+[0]*x+[-1])
pole.append([-1]*(x+2))


print(pole)
for i in range(1,x+1):
    canvas.create_line(0, 500/x*i, 500, 500/x*i)
    canvas.create_line(500/x*i, 0, 500/x*i, 500)

pocet_min = 0
while pocet_min < 3:
    rand_x = random.randrange(1,len(pole)-1)
    rand_y = random.randrange(1,len(pole)-1)
    if pole[rand_x][rand_y] != 9:
       pole[rand_x][rand_y] = 9
       pocet_min += 1

for i in range(1, len(pole)-1):
    for j in range(1, len(pole)-1):
        if pole[i][j] != 9:
            okolite_miny = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if pole[i+k][j+l] == 9:
                        okolite_miny += 1
            pole[i][j] = okolite_miny

def odkry():
    for y in range(1,len(pole)-1):
        for x in range(1,len(pole)-1):
            canvas.create_text(x*100-50, y*100-50,text=pole[y][x])
            if pole[y][x]==9:
                
                canvas.create_oval(x*100-100, y*100-100,x*100,y*100,fill='red')
                canvas.create_text(x*100-50, y*100-50,text=pole[y][x])
                canvas.create_text(250,250,text='Prehral si.',font='TimesNewRoman 50')
            else:
                canvas.create_oval(x*100-100, y*100-100,x*100,y*100,)
            
def ukaz_nuly(y, x):
    if pole[y][x] == 0:
            canvas.create_oval(x*w, y*w, x*w+w, y*w+w)
            canvas.create_text(x*w+w/2, y*w+w/2, text=pole[y+1][x*w+1])
            print("**nula**")
            

                    
def klik(a):
    print("x",a.x)
    print("y",a.y)
    if pole[a.y//w+1][a.x//w+1] == 9:
        canvas.create_oval(a.x//w*w, a.y//w*w, a.x//w*w+w, a.y//w*w+w,fill='red')
        canvas.create_text(a.x//w*w+w/2, a.y//w*w+w/2,text=pole[a.y//w+1][a.x//w+1])
        
        odkry()
        ukaz_nuly()
    else:            
        canvas.create_oval(a.x//w*w, a.y//w*w, a.x//w*w+w, a.y//w*w+w)
        canvas.create_text(a.x//w*w+w/2, a.y//w*w+w/2,text=pole[a.y//w+1][a.x//w+1])

    
def rklik(a):
    canvas.create_rectangle(a.x//w*w+500/x/4, a.y//w*w+500/x/4, a.x//w*w+w-500/x/2, a.y//w*w+w-500/x/2,fill='red')
    canvas.create_line(a.x//w*w+w-500/x/2, a.y//w*w+w-500/x/2, a.x//w*w+w-500/x/2, a.y//w*w+w)

canvas.bind("<Button-3>",rklik)
canvas.bind("<Button-1>",klik)
for i in range(len(pole)):
    print(pole[i])

canvas.mainloop()
