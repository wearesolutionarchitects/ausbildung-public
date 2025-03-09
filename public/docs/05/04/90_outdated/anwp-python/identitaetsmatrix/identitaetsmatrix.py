'''
Aufgabe:Schreiben Sie ein Python-Programm, das eine 4x4 Identitätsmatrix erstellt und ausgibt.
Eine Identitätsmatrix ist eine quadratische Matrix mit 1en auf der Hauptdiagonalen und 0en in allen anderen Positionen.

Hauptdioganle: 1 0 0 0
               0 1 0 0
               0 0 1 0
               0 0 0 1

4x4 Identitätsmatrix: 4 Zeilen, 4 Spalten [0
Column 1: 1 0 0 0 -  Spalten
Row 1:    0 1 0 0 -  Zeilen

PAP x
Pseudocode x

Schleifen ? ja
Entscheidung? if? ja

Eingabe? input()? nein 
Ausgabe? print()? -> Zeile
Berechnung? Formeln? -> Dimension = Dimension - 1
Datentypen? int
'''

# matrix = []
# matrix = [[1, 0, 0, 0], [0, 1, 0, 0]]

# reihe1 = [1, 0, 0, 0]
# reihe2 = [0, 1, 0, 0]
# reihe3 = [0, 0, 1, 0]
# reihe4 = [0, 0, 0, 1]

# print (reihe3)

#devied and counquer

#baue eine Zeile
#Zeile ist leer
#Zeile ist leer [] -> schleife
#füge Zahl in Zeile ein
#fuege zahl in zeile-liste ein # noch kein Durchlauf [0], 1. Durchlauf [1,0], 2. Durchlauf [1,0] ... [1,0,0,0]

""" dimension = 4
zeile = [] # Beginn mit leere Zeile / Zeile ist eine leere Liste mit leeren Zellen

    falls dimension == 4 -> 
        fuege 1 in die Zeile
    sonst fuege 0 in die Zeile ein
    
    dimension = dimension - 1 """


zeile = []
dimension = 4
while dimension > 0:
    if dimension == 4:
        zeile.append(1)
    else:
        zeile.append(0)
    dimension = dimension - 1

print(zeile)

