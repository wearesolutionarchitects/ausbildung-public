import enum

class Farbe(enum.IntEnum):
    ROT = 5
    GELB = 2
    BLAU = 4

print("Enumeration 'Farbe', Anzahl:", len(Farbe))
for f in Farbe:
    print("Name:", f.name, "Wert:", f.value)
f = 2
if f == Farbe.GELB:
    print("Das ist die Konstante GELB mit dem Wert 2")
print(Farbe.GELB)
print(Farbe.GELB * 10)
if 2 in Farbe:
    print("Wert 2 in 'Farbe'")
print()

class Figur(enum.IntEnum):
    KREIS = 3
    QUADRAT = enum.auto()
    LINIE = enum.auto()
    POLYGON = enum.auto()

print("Enumeration 'Figur', Anzahl:", len(Figur))
for f in Figur:
    print("Name:", f.name, "Wert:", f.value)
print()

class Wochentag(enum.StrEnum):
    MONTAG = "Montag"
    DIENSTAG = "Dienstag"
    MITTWOCH = "Mittwoch"

print("Enumeration 'Wochentag', Anzahl:", len(Wochentag))
for w in Wochentag:
    print("Name:", w.name, "Wert:", w.value)

