import random
random.seed()

a = random.randint(1,10)
b = random.randint(1,10)
c = a + b
print(f"Die Aufgabe: {a} + {b}")

for i in 1, 2, 3, 4:
    print("Bitte Lösungsvorschlag eingeben:")
    zahl = int(input())
    if zahl == c:
        print(zahl, "ist richtig")
        break
    else:
        print(zahl, "ist falsch")

print("Ergebnis:", c)
