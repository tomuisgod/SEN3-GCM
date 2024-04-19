retazec = "ahoj svet"

abc_tab = ["a", "h", "o", "j", " ", "s", "v", "e", "t"]
r_tab = ["b", "i", "k", "p", "f", "z", "x", "q", "p"]

for chr in retazec:
    print(r_tab[abc_tab.index(chr)], end="")
