import sys
try:
    d = open("daten.csv")
except:
    print("Datei nicht geöffnet")
    sys.exit(0)

tx = d.read()
d.close()
li = tx.split("\n")

for zeile in li:
    if zeile:
        ds = zeile.split(";")
        gh = str(ds[3]).replace(",", ".")
        print(f"{ds[0]} {ds[1]} {ds[2]} {gh} {ds[4]}")
