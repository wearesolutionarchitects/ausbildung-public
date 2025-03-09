while True:
    try:
        zahl = float(input("Eine positive Zahl: "))
        if zahl < 0:
            raise
        kw = 1.0 / zahl
        break
    except:
        print("Fehler")

print(f"Der Kehrwert von {zahl} ist {kw}")
