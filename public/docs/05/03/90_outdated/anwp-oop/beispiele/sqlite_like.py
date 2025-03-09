import os, sys, sqlite3
if not os.path.exists("firma.db"):
    print("Keine Datenbank")
    sys.exit(0)

connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM personen WHERE name LIKE 'm%'")
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

cursor.execute("SELECT * FROM personen WHERE name LIKE '%i%'")
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

cursor.execute("SELECT * FROM personen WHERE name LIKE 'M__er'")
for dsatz in cursor:
    print(dsatz[0], dsatz[1])

connection.close()
