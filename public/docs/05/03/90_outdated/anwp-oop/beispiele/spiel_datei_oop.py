import random, time, glob

class Spiel:
    def __init__(self):
        random.seed()
        self.richtig = 0
        self.anzahl = 5
        s = input("Bitte geben Sie Ihren Namen ein (max. 10 Zeichen): ")
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
    def __init__(self):
        self.liste = []
        if not glob.glob("highscore.csv"):
            return
        d = open("highscore.csv")
        zeile = d.readline()
        while zeile:
            teil = zeile.split(";")
            name = teil[0]
            zeit = teil[1]
            zeit = zeit.replace(",", ".")
            self.liste.append([name, float(zeit)])
            zeile = d.readline()
        d.close()

    def aendern(self, name, zeit):
        gefunden = False
        for i in range(len(self.liste)):
            if zeit < self.liste[i][1]:
                self.liste.insert(i, [name, zeit])
                gefunden = True
                break
        if not gefunden:
            self.liste.append([name, zeit])

    def speichern(self, name, zeit):
        self.aendern(name, zeit)
        d = open("highscore.csv", "w")
        for element in self.liste:
            name = element[0]
            zeit = str(element[1]).replace(".", ",")
            d.write(f"{name};{zeit}\n")
        d.close()

    def __str__(self):
        if not self.liste:
            return "Keine Highscores vorhanden"

        ausgabe = " P. Name            Zeit\n"
        for i in range(len(self.liste)):
            ausgabe += f"{i+1:2d}. {self.liste[i][0]:10}" \
                       f"{self.liste[i][1]:6.2f} sec\n"
            if i >= 9:
                break
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
