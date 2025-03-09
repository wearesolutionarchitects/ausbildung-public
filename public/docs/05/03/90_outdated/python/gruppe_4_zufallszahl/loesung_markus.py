def Aufgabe3Strukto():
    import random
    rateZahl = random.randint(0, 300)
    gefunden = False
    anzahlVersuche = 1
    while gefunden == False:
        userZahl = int(input("Zahl eingeben"))
        if userZahl < rateZahl:
            print("Zahl zu klein")
            anzahlVersuche += 1
        elif userZahl > rateZahl:
            print("Zahl zu groß")
            anzahlVersuche += 1
        elif userZahl == rateZahl:
            gefunden = True
    print(f"Anzahl der Versuche:{anzahlVersuche}.")
Aufgabe3Strukto()