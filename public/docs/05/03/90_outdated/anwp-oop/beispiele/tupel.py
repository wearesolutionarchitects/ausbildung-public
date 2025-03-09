z = (3, 6, -8)
print("Tupel 1 verpackt:", z)
z = 3, 6, -8
print("Tupel 2 verpackt:", z)

for i in 3, 6, -8:
    print(i)

a, b, c = z
print("Tupel entpackt:", a, b, c)

a, b, c = 3, 6, -8
print("Mehrfache Zuweisung:", a, b, c)

a, b, c = c, a, a+b
print("Auswirkung später:", a, b, c)

a, *b, c = 3, 6, 12, -28, -8
print("Rest in Liste:", a, b, c)
