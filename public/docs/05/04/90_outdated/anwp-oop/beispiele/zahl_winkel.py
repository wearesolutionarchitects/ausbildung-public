import math

x = 30
xbm = math.radians(x)
print(f"Sinus {x} Grad: {math.sin(xbm)}")
print(f"Kosinus {x} Grad: {math.cos(xbm)}")
print(f"Tangens {x} Grad: {math.tan(xbm)}")

z = 0.5
print(f"Arkussinus {z} in Grad: {math.degrees(math.asin(z))}")
z = 0.866
print(f"Arkuskosinus {z} in Grad: {math.degrees(math.acos(z))}")
z = 0.577
print(f"Arkustangens {z} in Grad: {math.degrees(math.atan(z))}")
