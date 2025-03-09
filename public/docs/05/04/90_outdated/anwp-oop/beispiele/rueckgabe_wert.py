# Definition der Funktion
def mittelwert(x,y):
    ergebnis = (x+y) / 2
    return ergebnis

# Programm
c = mittelwert(3, 9)
print("Mittelwert:", c)

x = 5
print("Mittelwert:", mittelwert(x,4))

y = -5.1
z = 2.8
print(f"Mittelwert: {mittelwert(y,z)}")
