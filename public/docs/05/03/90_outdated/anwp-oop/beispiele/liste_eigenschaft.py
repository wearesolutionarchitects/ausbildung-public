import random

z = [3, 6.2, -12]
print("Liste:", z)
print("Element:", z[0])
print("Slice:", z[:2])
print()

print("Schleife:")
for element in z:
      print(element)
print()

print("Schleife mit Index:")
for i in range(len(z)):
      print(f"{i}: {z[i]}")
print()

a = ["Paris", "Lyon"]
b = ["Rom", "Pisa"]
c = a + b * 2
print("Addiert und vervielfacht:", c)

print("Zufälliges Element:", random.choice(c))
random.shuffle(c)
print("Nach dem Mischen:", c)

