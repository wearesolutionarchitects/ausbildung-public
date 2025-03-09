import sys
try:
    d = open("formatiert.txt")
except:
    print("Datei nicht geöffnet")
    sys.exit(0)

dslaenge = 51
for i in range(3):
    d.seek(dslaenge*i)
    name = d.read(12).strip()
    d.seek(30 + dslaenge*i)
    gehalt = float(d.read(8))
    print(name, gehalt)

d.close()

