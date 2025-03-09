import numpy as np

a = np.array([[[2, 8],[3, 7]], [[5, 4],[9, 1]]])
b = a * 2
print("Operator und Skalar auf mehrdimensionalen Array anwenden:")
print(b)
print("Form des Arrays:", b.shape)
print()

c = np.matrix([[5, 2, 3],[8, 4, 5]])
print("Matrix c:")
print(c)
print("Form der Matrix:", c.shape)
print()

d = c * 2
print("Rechenoperation mit Skalar:")
print(d)
print()

e = np.matrix([[2, -4, 7],[-1, 9, 3]])
print("Matrix e:")
print(e)
print("Form der Matrix:", e.shape)
print()

f = c + e
print("Matrizenaddition c + e:")
print(f)
print()

g = np.matrix([[2, 3],[4, 5],[2, 6]])
print("Matrix g:")
print(g)
print("Form der Matrix:", g.shape)
print()

h = c * g
print("Matrizenmultiplikation c * g:")
print(h)
