import random
random.seed()

a = random.randint(1,10)
b = random.randint(1,10)
c = a + b
print(f"Die Aufgabe: {a} + {b}")

print("Bitte Lösungsvorschlag eingeben:")
zahl = int(input())
print("Ihre Eingabe:", zahl)
print("Das Ergebnis:", c)
