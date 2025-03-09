x = 12
y = 15
z = 20
print(f"x:{x}, y:{y}, z:{z}")

if x<y and x<z:
    print("x ist die kleinste Zahl")

if y>x or y>z:
    print("y ist nicht die kleinste Zahl")

if not y<x:
    print("y ist nicht kleiner als x")
