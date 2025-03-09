print("Bitte geben Sie eine ganze Zahl ein")
z = input()

try:
    zahl = int(z)
    print(f"Sie haben die ganze Zahl {zahl} eingegeben")
except Exception as e:
    print(e)
