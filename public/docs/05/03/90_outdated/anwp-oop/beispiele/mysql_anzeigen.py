import sys, mysql.connector
try:
    connection = mysql.connector.connect(host = "localhost", \
        user = "root", passwd = "", db = "firma")
except:
    print("Keine Verbindung zum Server oder keine Datenbank")
    sys.exit(0)

cursor = connection.cursor()
cursor.execute("SELECT * FROM personen")
result = cursor.fetchall()
cursor.close()
connection.close()

for datensatz in result:
    for feld in datensatz:
        print(f"{feld} ", end="")
    print()
