# Funktion aufgabe()
def aufgabe():
    a = random.randint(1,10)
    b = random.randint(1,10)
    print(f"Die Aufgabe: {a} + {b}")
    return a + b

# Funktion kommentar()
def kommentar(eingabezahl, ergebnis):
    if eingabezahl == ergebnis:
        print(eingabezahl, "ist richtig")
    else:
        print(eingabezahl, "ist falsch")

# Programm
import random
random.seed()
c = aufgabe()
zahl = c + 1
versuch = 0

while zahl != c:
    versuch = versuch + 1
    print("Bitte Lösungsvorschlag eingeben:")
    z = input()
    try:
        zahl = int(z)
    except:
        print("Sie haben keine ganze Zahl eingegeben")
        continue
    kommentar(zahl,c)

print("Ergebnis:", c)
print("Anzahl der Versuche:", versuch)
