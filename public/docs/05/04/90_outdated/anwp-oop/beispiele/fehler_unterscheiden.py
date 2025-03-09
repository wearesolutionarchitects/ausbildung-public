while True:
    try:
        zahl = float(input("Eine positive Zahl: "))
        if zahl == 0:
            raise RuntimeError("Zahl gleich 0")
        if zahl < 0:
            raise RuntimeError("Zahl zu klein")
        kw = 1.0 / zahl
        break
    except ValueError:
        print("Fehler: keine Zahl")
    except ZeroDivisionError:
        print("Fehler: Zahl 0 eingegeben")
    except RuntimeError as e:
        print("Fehler:", e)

print(f"Der Kehrwert von {zahl} ist {kw}")
