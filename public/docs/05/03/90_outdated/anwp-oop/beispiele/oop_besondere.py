class Fahrzeug:
    def __init__(self, bez="(leer)", ge=0):
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def __str__(self):
        return f"{self.bezeichnung} {self.geschwindigkeit} km/h"
    def __del__(self):
        print(f"Entfernt: {self}")
    def beschleunigen(self, wert):
        self.geschwindigkeit += wert

opel = Fahrzeug("Opel Admiral", 40)
renault = Fahrzeug("Renault Alpine")
fiat = Fahrzeug(ge=60)
mercedes = Fahrzeug()

print(opel)
print(renault)
print(fiat)
print(mercedes)

opel.beschleunigen(20)
print(opel.__dict__)
del opel
# print(opel)
