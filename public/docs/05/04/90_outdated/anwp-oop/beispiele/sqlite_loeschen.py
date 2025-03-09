import os, sys, sqlite3
if not os.path.exists("firma.db"):
    print("Keine Datenbank")
    sys.exit(0)

def ausgabe():
    sql = "SELECT * FROM personen"
    cursor.execute(sql)
    for dsatz in cursor:
        print(dsatz[0], dsatz[1], dsatz[2], dsatz[3])
    print()

connection = sqlite3.connect("firma.db")
cursor = connection.cursor()
ausgabe()

sql = "DELETE FROM personen WHERE personalnummer = 8339"
cursor.execute(sql)
connection.commit()

ausgabe()
connection.close()


