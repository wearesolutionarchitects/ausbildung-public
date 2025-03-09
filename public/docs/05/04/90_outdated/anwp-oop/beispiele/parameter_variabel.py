def summe(a, *summanden):
    erg = a
    for s in summanden:
        erg += s
    return erg

print("Summe:", summe(3, 4))
print("Summe:", summe(3, 8, 12, -5))
