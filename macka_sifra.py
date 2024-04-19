# Ascii posun sifra

retazec = "ahoj svet".lower()
heslo = "macka".lower()

nretazec = []

i = 0
for char in retazec:
    ascii_shift = 122-ord(heslo[i%len(heslo)])
    if ord(char) + ascii_shift >122:
        ascii_shift = 122-ord(char) - ascii_shift
    nretazec.append(chr(ord(char)+ascii_shift))
    i += 1

retazec = ""
for ch in nretazec:
    retazec += ch

print(retazec) # nacy9mack
