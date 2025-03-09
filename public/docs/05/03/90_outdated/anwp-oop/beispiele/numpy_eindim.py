import numpy as np

a = np.array([5, 8, -4])
print("Eindimensionaler Array = Vektor:", a)

b = a * 2
print("Rechenoperation mit Skalar:", b)

c = np.linspace(0, 30, 4)
print("Array mit äquidistanten Werten:", c)

d = np.sin(np.radians(c))
print("Funktion auf Array anwenden:", d)

e = np.array([2, 8, 3])
f = np.array([3, 7, -4])
g = e + f
print("Vektoraddition:", g)

h = e @ f
print("Skalarprodukt:", h)

i = np.cross(e, f)
print("Kreuzprodukt:", i)

