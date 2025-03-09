import json, sys

class Fahrzeug:
    def __init__(self, bez, ge):
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def __str__(self):
        return f"{self.bezeichnung} {self.geschwindigkeit} km/h"

try:
    d = open("json_datei.json", "w")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

s = set([8, 5, 2, 5])
ls = []
for element in s:
    ls.append(element)

opel = Fahrzeug("Opel Admiral", 40)

tu = [4,"abc",8], -12.5, {"a":1, "b":1}, ls, opel.__dict__
json.dump(tu, d)
d.close()
