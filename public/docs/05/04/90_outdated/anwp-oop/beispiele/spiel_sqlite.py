import random, time, glob, sqlite3

def hs_anzeigen():
    if not glob.glob("highscore.db"):
        print("Keine Highscores vorhanden")
        return

    con = sqlite3.connect("highscore.db")
    cursor = con.cursor()
    sql = "SELECT * FROM daten ORDER BY zeit LIMIT 10"
    cursor.execute(sql)

    print(" P. Name            Zeit")
    i = 1
    for dsatz in cursor:
        print(f"{i:2d}. {dsatz[0]:10} {dsatz[1]:5.2f} sec")
        i = i+1
    con.close()

def spiel():
    name = input("Bitte geben Sie Ihren Namen ein (max. 10 Zeichen): ")
    name = name[0:10]

    richtig = 0
    startzeit = time.time()

    for aufgabe in range(5):
        a = random.randint(10,30)
        b = random.randint(10,30)
        c = a + b

        try:
            zahl = int(input(f"Aufgabe {aufgabe+1} von 5: {a} + {b} : "))
            if zahl == c:
                print("*** Richtig ***")
                richtig += 1
            else:
                raise
        except:
            print("* Falsch *")

    differenz = time.time() - startzeit
    print(f"Ergebnis: {richtig} von 5 in {differenz:.2f} sec", end="")
    if richtig == 5:
        print(", Highscore")
    else:
        print(", leider kein Highscore")
        return

    if not glob.glob("highscore.db"):
        con = sqlite3.connect("highscore.db")
        cursor = con.cursor()
        sql = "CREATE TABLE daten(name TEXT, zeit REAL)"
        cursor.execute(sql)
        con.close()

    con = sqlite3.connect("highscore.db")
    cursor = con.cursor()
    sql = f"INSERT INTO daten VALUES('{name}', {differenz})"
    cursor.execute(sql)
    con.commit()
    con.close()

    hs_anzeigen()

# Programm
random.seed()

while True:
    try:
        menu = int(input("Bitte eingeben "
            "(0: Ende, 1: Highscores, 2: Spielen): "))
    except:
        print("Falsche Eingabe")
        continue

    if menu == 0:
        break
    elif menu == 1:
        hs_anzeigen()
    elif menu == 2:
        spiel()
    else:
        print("Falsche Eingabe")
