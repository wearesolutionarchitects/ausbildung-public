import random
random.seed()

a = random.randint(1,10)
b = random.randint(1,10)
c = a + b
print(f"Die Aufgabe: {a} + {b}")

zahl = c + 1
versuch = 0
while zahl != c:
    versuch = versuch + 1
    print("Bitte Lösungsvorschlag eingeben:")
    zahl = int(input())
    if zahl == c:
        print(zahl, "ist richtig")
    else:
        print(zahl, "ist falsch")

print("Ergebnis:", c)
print("Anzahl der Versuche:", versuch)
