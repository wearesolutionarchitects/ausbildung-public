def volumen(breite, laenge, tiefe, farbe):
    print("Werte:", breite, laenge, tiefe, farbe)
    print("Volumen:", breite * laenge * tiefe, "Farbe:", farbe)

volumen(4, 6, 2, "Rot")
volumen(laenge=2, farbe="Gelb", tiefe=7, breite=3)
volumen(5, tiefe=2, laenge=8, farbe="Blau")
# volumen(3, tiefe=4, laenge=5, "Schwarz")
