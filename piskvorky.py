import tkinter
import random

# Pocet vertikalnych a diagonalnych riadkov
a = int(input("Zadaj počet polí: "))

canvas = tkinter.Canvas(width=100*a, height=100*a)
canvas.pack()
 


# Pole
for v in range(a-1):
    canvas.create_line(100*(v+1), 0, 100*(v+1), 100*a, width= 5)

for d in range(a-1):
    canvas.create_line(0, 100*(d+1), 100*a, 100*(d+1), width= 5)





tkinter.mainloop()
