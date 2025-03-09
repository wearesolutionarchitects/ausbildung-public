import copy
class Fahrzeug:
    def __init__(self, bez, ge):
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def beschleunigen(self, wert):
        self.geschwindigkeit += wert
def __str__(self):
    return f"{self.bezeichnung} {self.geschwindigkeit} km/h"
opel = Fahrzeug("Opel Admiral", 40)
print("Original:", opel)
print()
opel2 = Fahrzeug(opel.bezeichnung, opel.geschwindigkeit)
opel2.beschleunigen(30)
print("Kopie:", opel2)
print("Identität", opel is opel2)
print()
opel3 = copy.deepcopy(opel)
opel3.beschleunigen(35)
print("Kopie:", opel3)
print("Identität:", opel is opel3)
print()
opel4 = opel
opel4.beschleunigen(40)
print("Referenz:", opel4)
print("Identität:", opel is opel4)