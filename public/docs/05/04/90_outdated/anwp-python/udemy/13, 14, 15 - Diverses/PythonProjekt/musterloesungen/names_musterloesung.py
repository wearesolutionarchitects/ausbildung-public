# Aufgabe:
#
# Im Ordner "names" gibt es einige Textdateien, die Namen von Personen enthalten (zufällig generiert).
#
# Aufgabe:
#   Schreibe ein Programm, welches alle Textdateien aus dem Ordner "names" einliest, und ermittelt, wie oft der Name
#   "Max" insgesamt in allen Dateien vorkommt.
#
# Beispiel:
#   Käme der Name "Max" in der Datei "1.txt" 1x vor, und in der Datei "2.txt" 2x, sonst aber nie, soll das Programm
#   die Zahl 3 ausgeben.

import os

folder = os.path.join(os.path.dirname(__file__), "names")

files = os.listdir(folder)

counter = 0

for filename in files:
    f = os.path.join(os.path.dirname(__file__), "names", filename)
    with open(f, "r", encoding="utf-8") as file:
        for line in file:
            l = line.strip().split(" ")
            firstname = l[0]
            if firstname == "Max":
                counter = counter + 1

print(counter)
