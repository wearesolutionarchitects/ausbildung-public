z = ["Paris", "Nantes", "Lyon", "Metz"]
print("Liste:", z)

z.sort()
print("Sortieren nach Text:", z)
print()

z = [12, 7, 38, -5]
print("Liste:", z)

z.sort()
print("Sortieren nach Zahlen:", z)

z.insert(1, 16)
print("Einsetzen:", z)

z.reverse()
print("Umdrehen:", z)

such = 16
if such in z:
    z.remove(such)
    print("Entfernen:", z)

z.append(12)
print("Am Ende hinzu:", z)
print()

such = 12
print(f"Anzahl gefunden:", z.count(such))

startpos = 0
while such in z[startpos:]:
    pos = z.index(12, startpos)
    print("Position:", pos)
    startpos = pos + 1
