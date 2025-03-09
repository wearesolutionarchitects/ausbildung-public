import os, sys, sqlite3
if not os.path.exists("firma.db"):
    print("Keine Datenbank")
    sys.exit(0)

connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

eingabeName = input("Bitte den gesuchten Nachnamen eingeben: ")
eingabeVorname = input("Bitte den gesuchten Vornamen eingeben: ")
sql = "SELECT * FROM personen WHERE name LIKE ? OR vorname LIKE ?"
cursor.execute(sql, (eingabeName, eingabeVorname))
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

eingabe = input("Bitte den gesuchten Namensteil eingeben: ")
sql = "SELECT * FROM personen WHERE name LIKE ?"
eingabe = "%" + eingabe + "%"
cursor.execute(sql, (eingabe,))
for dsatz in cursor:
    print(dsatz[0], dsatz[1])

connection.close()
