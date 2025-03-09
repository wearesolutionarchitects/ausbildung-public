import pickle, sys
class Fahrzeug:
    def __init__(self, bez, ge):
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def __str__(self):
        return f"{self.bezeichnung} {self.geschwindigkeit} km/h"

try:
    d = open("pickle_datei.bin", "wb")
except:
    print("Datei nicht geöffnet")
    sys.exit(0)

tu = [4,"abc",8], -12.5, {"a":1, "b":1}, set([8, 5, 2, 5])
pickle.dump(tu, d)

opel = Fahrzeug("Opel Admiral", 40)
pickle.dump(opel, d)

pickle.dump(3, d)
pickle.dump("Berlin", d)
pickle.dump("Hamburg", d)
pickle.dump("Dortmund", d)

d.close()
