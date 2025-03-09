inch = 2.54

while True:
    print("Bitte geben Sie den Inch-Wert ein")
    xi = input()

    try:
        xi = float(xi)
        break
    except:
        print("Falsche Eingabe")

xcm = xi * inch
print(f"{xi} Inch = {xcm} cm")



