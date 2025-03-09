class Fahrzeug:
    geschwindigkeit = 0
    def beschleunigen(self, wert):
        self.geschwindigkeit += wert
    def ausgabe(self):
        print("Geschwindigkeit:", self.geschwindigkeit)

volvo = Fahrzeug()
opel = Fahrzeug()

volvo.ausgabe()
volvo.beschleunigen(20)
volvo.ausgabe()

opel.ausgabe()


