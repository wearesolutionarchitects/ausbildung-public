import decimal

a = 10 / 7
print("float-Wert:  ", a)
a = decimal.Decimal(10) / 7
print("Decimal-Wert:", a)
print("Typ:", type(a))
print()

print("Ganze Zahlen:", a + 2 * 3 - (12 - 2) // 2)
print("Zahlen mit Nachkommastellen:", a + decimal.Decimal(2.5))
print("Division:", a + decimal.Decimal(4 / 2))
print()

a = decimal.Decimal(24)
print("Wert von a:", a)
print("Quadratwurzel von a:", a.sqrt())
print()

print("Natürlicher Logarithmus von a:", a.ln())
print("e hoch 3.178:", decimal.Decimal(3.178).exp())
print()

print("10er-Logarithmus von a:", a.log10())
print("Umdrehung:", 10 ** decimal.Decimal(a.log10()))


