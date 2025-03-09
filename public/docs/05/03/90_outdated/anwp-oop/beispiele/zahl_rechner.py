import math

print("Quadratwurzel von 64:", math.sqrt(64))
print("Kubikwurzel von -27:", math.cbrt(-27))
print("Ganzzahlige Quadratwurzel von 80:", math.isqrt(80))
print()

print("Natürlicher Logarithmus von 33:", math.log(33))
print("e hoch 3.5:", math.exp(3.5))
print("2 hoch 10:", math.exp2(10))
print()

print("10er-Logarithmus von 0.001:", math.log10(0.001))
print("10 ** -3:", 10 ** -3)
print()

print("Kreiszahl pi:", math.pi)
print("Eulersche Zahl e:", math.e)
print()

t1 = 3, 2, 5
t2 = 2, 4, 3
print("Produkt:", math.prod(t1))
print("Summe der Produkte:", math.sumprod(t1, t2))

print("Fakultät von 5:", math.factorial(5))
print("Größter gem. Teiler von 60 und 135:", math.gcd(60, 135))
print("Rest:", math.remainder(10.9, 2.5))
print("Rest:", math.remainder(11.9, 2.5))
print()

if not math.isclose(3, 2.96, rel_tol=0.01):
    print("Nicht nahe dran")

if math.isclose(3, 2.97, rel_tol=0.01):
    print("Nahe dran")
