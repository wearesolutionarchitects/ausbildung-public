inch = 2.54

print("Bitte geben Sie den Inch-Wert ein:")
xi = float(input())

while xi != 0:
    xcm = xi * inch
    print(f"{xi} Inch = {xcm} cm")
    print("Bitte geben Sie den Inch-Wert ein:")
    xi = float(input())

