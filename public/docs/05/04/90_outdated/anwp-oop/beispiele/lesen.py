import sys

def oeffnen():
    global d
    try:
        d = open("lesen.txt")
    except:
        print("Datei nicht geöffnet")
        sys.exit(0)

def wert(zeile):
    try:
        return float(zeile)
    except:
        return 0.0

oeffnen()
li = d.readlines()
summe = 0
for zeile in li:
    summe += wert(zeile)
print("Summe:", summe)
d.close()

oeffnen()
summe = 0
zeile = d.readline()
while zeile:
    summe += wert(zeile)
    zeile = d.readline()
print("Summe:", summe)
d.close()

oeffnen()
tx = d.read()
li = tx.split("\n")
summe = 0
for zeile in li:
    summe += wert(zeile)
print("Summe:", summe)
d.close()
