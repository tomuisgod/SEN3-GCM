import tkinter

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

s_p = 1000 / 10

x = 8
w = 500 // x

for i in range(1, x + 1):
    for j in range(1, x + 1):
        color = "black" if (i + j) % 2 == 0 else "white"
        canvas.create_rectangle((j - 1) * w, (i - 1) * w, j * w, i * w, fill=color)

        # x
        canvas.create_line(0, 500 / x * i, 500, 500 / x * i)
        # y
        canvas.create_line(500 / x * i, 0, 500 / x * i, 500)


tkinter.mainloop()
