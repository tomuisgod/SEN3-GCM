import tkinter
import random

canvas = tkinter.Canvas(width=1000, height=1000)
canvas.pack()

def hracie_pole():
    #Hracie pole
    canvas.create_line(400, 200, 400, 800, width=5)
    canvas.create_line(600, 200, 600, 800, width=5)
    canvas.create_line(200, 400, 800, 400, width=5)
    canvas.create_line(800, 600, 200, 600, width=5)

    #Text
    canvas.create_text(500, 50, text=a, font=('Helvetica 40 bold'))

def vyber_hraca():
    v = input("Pre vybratie kruhu stlac [A], pre vybratie kriziku stlac [B]")
    if len(v) < 1:
        print("Nevybral si si žiadnu možnosť, skús to prosím znova")
        v = input("Pre vybratie kruhu stlac [A], pre vybratie kriziku stlac [B]")

    if v != "A" or "B":
        print("Zvolená možnosť neexistuje, možnosti sú [A] pre kruh a [B] pre krizik")
        v = input("Pre vybratie kruhu stlac [A], pre vybratie kriziku stlac [B]")

    else:
        hracie_pole()
        if v == "A" or "a":
            kruh = 1
            krizik = 0
        if v == "B" or "b":
            kruh = 0
            krizik = 1


vyber_hraca


tkinter.mainloop()
