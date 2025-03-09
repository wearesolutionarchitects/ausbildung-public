def sortieren(eins, zwei):
    if eins > zwei:
        return zwei, eins
    else:
        return eins, zwei

x = 12
y = 7
print(f"x: {x}, y: {y}")
x, y = sortieren(x, y)
print(f"x: {x}, y: {y}")
