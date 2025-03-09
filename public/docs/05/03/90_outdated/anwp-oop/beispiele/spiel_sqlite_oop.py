import random, time, glob, sqlite3

class Spiel:
    def __init__(self):
        random.seed()
        self.richtig = 0
        self.anzahl = 5
        s = input("Bitte geben Sie Ihren "
            "Namen ein (max. 10 Zeichen): ")
        self.name = s[0:10]

    def spielen(self):
        for i in range(1,self.anzahl+1):
            a = Aufgabe(i, self.anzahl)
            print(a)
            self.richtig += a.beantworten()

    def messen(self, start):
        if start:
            self.startzeit = time.time()
        else:
            self.zeit = round(time.time() - self.startzeit, 2)

    def __str__(self):
        ausgabe = f"Richtig: {self.richtig} von" \
                  f" {self.anzahl} in {self.zeit} Sekunden"
        if self.richtig == self.anzahl:
            ausgabe += ", Highscore"
            hs = Highscore()
            hs.speichern(self.name, self.zeit)
            print(hs)
        else:
            ausgabe += ", leider kein Highscore"
        return ausgabe

class Aufgabe:
    def __init__(self, i, anzahl):
        self.nr = i
        self.anzahl = anzahl

    def __str__(self):
        a = random.randint(10,30)
        b = random.randint(10,30)
        self.ergebnis = a + b
        return f"Aufgabe {self.nr} von {self.anzahl}: {a} + {b}"
        
    def beantworten(self):
        try:
            if self.ergebnis == int(input()):
                print(f"{self.nr}: *** Richtig ***")
                return 1
            else:
                raise
        except:
            print(f"{self.nr}: *** Falsch ***")
            return 0

class Highscore:
    def speichern(self, name, zeit):
        if not glob.glob("highscore.db"):
            con = sqlite3.connect("highscore.db")
            cursor = con.cursor()
            sql = "CREATE TABLE daten(name TEXT, zeit REAL)"
            cursor.execute(sql)
            con.close()

        con = sqlite3.connect("highscore.db")
        cursor = con.cursor()
        sql = f"INSERT INTO daten VALUES('{name}', {zeit})"
        cursor.execute(sql)
        con.commit()
        con.close()

    def __str__(self):
        if not glob.glob("highscore.db"):
            return "Keine Highscores vorhanden"

        con = sqlite3.connect("highscore.db")
        cursor = con.cursor()
        sql = "SELECT * FROM daten ORDER BY zeit LIMIT 10"
        cursor.execute(sql)

        ausgabe = " P. Name            Zeit\n"
        i = 1
        for dsatz in cursor:
            ausgabe += f"{i:2d}. {dsatz[0]:10} {dsatz[1]:5.2f} sec\n"
            i = i+1

        con.close()
        return ausgabe

# Programm
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
        hs = Highscore()
        print(hs)
    elif menu == 2:
        s = Spiel()
        s.messen(True)
        s.spielen()
        s.messen(False)
        print(s)
    else:
        print("Falsche Eingabe")
