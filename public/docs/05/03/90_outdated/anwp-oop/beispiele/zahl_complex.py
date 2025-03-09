a = 2.5 - 4.2j
print(f"a = {a}, Typ: {type(a)}")
print(f"Realteil: {a.real}, Imaginärteil: {a.imag}")
print("Betrag:", abs(a))
print("Konjugiert komplex:", a.conjugate())
print()

b = 3.7j
print("b =", b)
print(f"Realteil: {b.real}, Imaginärteil: {b.imag}")
print("Betrag:", abs(b))
print()

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a ** 2.5 =", a ** 2.5)
print("5.1 + a / 3.2j * 2.8 =", 5.1 + a / 3.2j * 2.8)
print()

c = 2.5 - 4.2j
print("c =", c)
print("a == c:", a == c)
print("b != c:", b != c)
print()

c = 1j
print("c =", c)
print("c * c =", c * c)
