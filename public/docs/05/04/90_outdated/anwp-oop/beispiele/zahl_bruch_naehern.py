import fractions

x = 1.84953
print("Zahl:", x)

b3 = fractions.Fraction(x)
print("Fraction-Objekt:", b3)

b4 = b3.limit_denominator(100)
print("Approximiert auf Nenner max. 100:", b4)

wert = b4.numerator / b4.denominator
print("Wert:", wert)
print("rel. Fehler:", abs((x-wert)/x))
