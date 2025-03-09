import random

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

    def __str__(self):
        return f"Richtig: {self.richtig} von {self.anzahl}"

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
s.spielen()
print(s)
