while True:
    print("Bitte geben Sie eine ganze Zahl ein")
    z = input()
    try:
        zahl = int(z)
        print(f"Sie haben die ganze Zahl {zahl} eingegeben")
        break
    except:
        print("Fehler bei Umwandlung der Eingabe")
