import random, time

class Spiel:
    def __init__(self):
        random.seed()
        self.richtig = 0
        self.anzahl = -1
        while self.anzahl<1 or self.anzahl>10:
            try:
                print("Wie viele Aufgaben (1 bis 10):")
                self.anzahl = int(input())
            except:
                continue

    def spielen(self):
        for i in range(self.anzahl):
            a = Aufgabe(i+1, self.anzahl)
            print(a)
            self.richtig += a.beantworten()

    def messen(self, start):
        if start:
            self.startzeit = time.time()
        else:
            self.zeit = time.time() - self.startzeit

    def __str__(self):
        datum = time.strftime("%d.%m.%Y")
        uhrzeit = time.strftime("%H:%M:%S")
        return f"Richtig: {self.richtig} von {self.anzahl} " \
               f"in {self.zeit:.2f} Sekunden\nam {datum} um {uhrzeit}" 

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

s = Spiel()
s.messen(True)
s.spielen()
s.messen(False)
print(s)

