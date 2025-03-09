ta = "Das"
print("Text:", ta)
print("Typ:", type(ta))
print("Anzahl der Zeichen:", len(ta))
for z in ta:
    print(z)
for i in range(len(ta)):
    print(f"{i}: {ta[i]}")

tb = 'Auch das ist eine Zeichenkette'
print(tb)

tc = """Diese Zeichenkette
        steht in
        mehreren Zeilen"""
print(tc)

td = 'Hier sind "doppelte Hochkommata" gespeichert'
print(td)
