'''connectieren einer MSSQL Datenbank '''

#diese Klasse wird für die Connectierung benötigt
import pyodbc

# Verbindungsdaten
server = '172.29.40.28\\SQLEXPRESS'
database = 'videogames'
username = 'sa'
password = 'test'
driver = '{ODBC Driver 17 for SQL Server}'  # Beispiel für den Treibernamen, an deine Version anpassen

# Verbindungsaufbau Connectionstring z. B. C#
with pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
    # Instanzieren eines cursorss
    cursor = conn.cursor()
    
    # Tabelle erstellen (Beispiel)
    cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Produkte' and xtype='U')
        CREATE TABLE Produkte (id INT PRIMARY KEY, name NVARCHAR(250), quantity INT)
    ''')
    conn.commit()

    # Daten einfügen
    cursor.execute("INSERT INTO Produkte (id, name, quantity) VALUES (?, ?, ?)", (1, 'Game of Heiko', 20))
    cursor.execute("INSERT INTO Produkte (id, name, quantity) VALUES (?, ?, ?)", (2, 'Game of Markus', 24))
    cursor.execute("INSERT INTO Produkte (id, name, quantity) VALUES (?, ?, ?)", (3, 'Game of IBB', 25))
    conn.commit()

    # Daten abfragen
    cursor.execute("SELECT * FROM Produkte")
    for row in cursor:
        print(row)
