import os, sys, sqlite3
if not os.path.exists("firma.db"):
    print("Keine Datenbank")
    sys.exit(0)

connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

cursor.execute("SELECT name, vorname FROM personen")
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

cursor.execute("SELECT * FROM personen WHERE gehalt > 3600")
for dsatz in cursor:
    print(dsatz[0], dsatz[3])
print()

cursor.execute("SELECT * FROM personen WHERE name = 'Schmitz'")
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

cursor.execute("SELECT * FROM personen WHERE gehalt >= 3600 AND gehalt <= 3650")
for dsatz in cursor:
    print(dsatz[0], dsatz[3])

connection.close()
