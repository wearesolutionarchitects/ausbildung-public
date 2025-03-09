import os, sys, sqlite3
if not os.path.exists("firma.db"):
    print("Keine Datenbank")
    sys.exit(0)

connection = sqlite3.connect("firma.db")
cursor = connection.cursor()
sql = "SELECT * FROM personen"
cursor.execute(sql)

for dsatz in cursor:
    print(dsatz[0], dsatz[1], dsatz[2], dsatz[3], dsatz[4])
connection.close()
