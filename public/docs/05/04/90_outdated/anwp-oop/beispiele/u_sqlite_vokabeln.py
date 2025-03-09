import os, sys, sqlite3, random

# Datenbank und Liste erzeugen, falls Datenbank nicht vorhanden
def erzeugen():
    li = [[1, "Bedingung", "condition"],
          [2, "suchen", "to look for"],
          [3, "Werbeanzeige", "advertisement"],
          [4, "abkürzen", "to abbreviate"],
          [5, "nützlich", "useful"],
          [6, "Wirkung", "effect"],
          [7, "beraten", "to advise"],
          [8, "übersetzen", "to translate"],
          [9, "einfach", "easy"],
          [10, "ankündigen", "to announce"]]
    connection = sqlite3.connect("lernen.db")
    cursor = connection.cursor()
    sql = "CREATE TABLE vokabel(id INTEGER PRIMARY KEY, deutsch TEXT, englisch TEXT)"
    cursor.execute(sql)
    for z in li:
        sql = "INSERT INTO vokabel VALUES(" + str(z[0]) + ", '" + z[1] + "', '" + z[2] + "')"
        cursor.execute(sql)
        connection.commit()
    connection.close()
    return li

# Liste erzeugen, falls Datenbank vorhanden
def laden():
    li = []
    connection = sqlite3.connect("lernen.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM vokabel"
    cursor.execute(sql)
    for dsatz in cursor:
        li.append([dsatz[0], dsatz[1], dsatz[2]])
    connection.close()
    return li

# Liste anzeigen
def alle(li):
    for z in li:
        print(z[0], "/", z[1], "/", z[2])

# Einzelne Elemente anzeigen
def lernen(li):
    z = random.choice(li)
    print(z[1], "/", z[2])

# Testen, bis Liste leer ist
def test(li):
    while(li):
        x = random.randint(0, len(li) - 1)
        antwort = input("Bitte übersetzen: '" + li[x][1] + "' ==> ")
        if antwort == li[x][2]:
            print("Richtig, Vokabel wird aus dem Test genommen")
            del li[x]
        else:
            print("Leider falsch, richtig wäre: " + li[x][2])
    print("Test erfolgreich beendet")

# Hauptprogramm
random.seed()

# Liste erzeugen, ggf. Datenbank erzeugen
if not os.path.exists("lernen.db"):
    li = erzeugen()
else:
    li = laden()

# Schleife bis Beendigung
aktiv = True
while(aktiv):
    auswahl = -1
    while not 0 <= auswahl <= 3: 
        auswahl = int(input("Ihre Auswahl: 0 (= Ende), 1 (= Alle), 2 (= Lernen), 3 (= Test): "))
    if auswahl == 0:
        aktiv = False
        break
    elif auswahl == 1:
        alle(li)
    elif auswahl == 2:
        lernen(li)
    else:
        test(li)

