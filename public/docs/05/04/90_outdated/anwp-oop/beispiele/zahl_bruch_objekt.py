import fractions

b1 = fractions.Fraction(12, 28)
print("Fraction-Objekt:", b1, type(b1))
print(f"Zähler: {b1.numerator}, Nenner: {b1.denominator}")
print(f"Wert: {b1:.12f}")
print()

x = 2.375
print("Zahl:", x)
b2 = fractions.Fraction(x)
print("Fraction-Objekt:", b2)
print()

b3 = fractions.Fraction("350_000 /280_000")
print("Aus String:", b3)
print("Ganzzahlig:", b3.is_integer())
print(f"Formatiert: {b3:.3f}")
