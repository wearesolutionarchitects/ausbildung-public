import sys, mysql.connector
try:
    connection = mysql.connector.connect \
        (host = "localhost", user = "root", passwd = "")
except:
    print("Keine Verbindung zum Server")
    sys.exit(0)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS firma")
connection.commit()

cursor.execute("USE firma")
connection.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS personen"
      "(name VARCHAR(30), vorname VARCHAR(25),"
      "personalnummer INT(11), gehalt DOUBLE, "
      "geburtstag DATE, PRIMARY KEY (personalnummer))"
      "ENGINE=InnoDB DEFAULT CHARSET=UTF8")
connection.commit()

try:
    cursor.execute("INSERT INTO personen VALUES('Maier', " \
        "'Hans', 6714, 3500, '1962-03-15')")
    connection.commit()
    cursor.execute("INSERT INTO personen VALUES('Schmitz', " \
        "'Peter', 81343, 3750, '1958-04-12')")
    connection.commit()
    cursor.execute("INSERT INTO personen VALUES('Mertens', " \
        "'Julia', 2297, 3621.5, '1959-12-30')")
    connection.commit()
except:
    print("Fehler beim Erstellen")

cursor.close()
connection.close()
