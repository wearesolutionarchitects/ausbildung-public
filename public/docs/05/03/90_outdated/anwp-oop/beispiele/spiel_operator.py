import random
random.seed()

a = random.randint(1,10)
b = random.randint(1,10)
c = a + b
print(f"Die Aufgabe: {a} + {b}")

print("Bitte Lösungsvorschlag eingeben:")
zahl = int(input())

if zahl == c:
    print(zahl, "ist richtig")
elif zahl < 0 or zahl > 100:
    print(zahl, "ist weit daneben")
elif c-1 <= zahl <= c+1:
    print(zahl, "ist nahe dran")
else:
    print(zahl, "ist falsch")

print("Ergebnis:", c)
