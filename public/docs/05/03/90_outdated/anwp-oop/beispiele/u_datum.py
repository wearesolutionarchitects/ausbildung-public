print("Tag des Datums eingeben:")
tag = int(input())
print("Monat des Datums eingeben:")
monat = int(input())
print("Jahr des Datums eingeben:")
jahr = int(input())
richtig = True

if tag < 1 or tag > 31:
    richtig = False
elif monat < 1 or monat > 12:
    richtig = False
elif monat == 4 or monat == 6 or monat == 9 or monat == 11:
    print("Letzter Tag: 30")
    if tag > 30:
        richtig = False
elif monat == 2:
    if jahr%4 == 0 and jahr%100 != 0 or jahr%400 == 0:
        print("Letzter Tag: 29")
        if tag > 29:
            richtig = False
    else:
        print("Letzter Tag: 28")
        if tag > 28:
            richtig = False
else:
    print("Letzter Tag: 31")

if richtig:
    print("Gültiges Datum")
else:
    print("Ungültiges Datum")
