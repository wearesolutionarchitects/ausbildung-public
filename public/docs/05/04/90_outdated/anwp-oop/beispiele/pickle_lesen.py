import pickle, sys
class Fahrzeug:
    def __init__(self, bez, ge):
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def __str__(self):
        return f"{self.bezeichnung} {self.geschwindigkeit} km/h"

try:
    d = open("pickle_datei.bin", "rb")
except:
    print("Datei nicht geöffnet")
    sys.exit(0)

tu = pickle.load(d)
print(tu)

opel = pickle.load(d)
opel.geschwindigkeit += 20
print(opel)

anzahl = pickle.load(d)
for i in range(anzahl):
    print(pickle.load(d))

d.close()
