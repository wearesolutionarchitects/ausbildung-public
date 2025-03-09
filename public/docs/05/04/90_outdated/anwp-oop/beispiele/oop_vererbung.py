class Fahrzeug:
    def __init__(self, bez, ge):
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def beschleunigen(self, wert):
        self.geschwindigkeit += wert
    def __str__(self):
        return f"{self.bezeichnung} {self.geschwindigkeit} km/h"

class PKW(Fahrzeug):
    def __init__(self, bez, ge, ins):
        super().__init__(bez, ge)
        self.insassen = ins
    def __str__(self):
        return f"{super().__str__()} {self.insassen} Insassen"
    def einsteigen(self, anzahl):
        self.insassen += anzahl
    def aussteigen(self, anzahl):
        self.insassen -= anzahl

fiat = PKW("Fiat Marea", 50, 0)
fiat.einsteigen(3)
fiat.aussteigen(1)
fiat.beschleunigen(10)
print(fiat)
