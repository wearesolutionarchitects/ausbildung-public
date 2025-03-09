def hochzwei(x):
    return x * x

def hochdrei(x):
    return x * x * x

def ausgabe(unten, oben, schritt, f):
    for x in range(unten, oben, schritt):
        print(x, ":", f(x), sep="", end=" ")
    print()

# Programm
ausgabe(1, 5, 1, hochzwei)
ausgabe(1, 5, 1, hochdrei)
ausgabe(1, 5, 1, lambda x: x * x * x * x)
