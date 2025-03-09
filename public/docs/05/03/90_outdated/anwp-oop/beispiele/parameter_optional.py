def volumen(breite, laenge, tiefe=1, farbe="Schwarz"):
    print("Werte:", breite, laenge, tiefe, farbe)
    print("Volumen:", breite * laenge * tiefe, "Farbe:", farbe)

volumen(4, 6, 2, "Rot")
volumen(2, 12, 7)
volumen(5, 8)
volumen(4, 7, farbe="Rot")
