import json, sys

class Fahrzeug:
    def __init__(self, bez, ge):
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def __str__(self):
        return f"{self.bezeichnung} {self.geschwindigkeit} km/h"

try:
    d = open("json_datei.json", "r")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

li = json.load(d)
d.close()

s = set()
for element in li[3]:
    s.add(element)

opel = Fahrzeug(li[4]["bezeichnung"], li[4]["geschwindigkeit"])

tu = li[0], li[1], li[2], s, opel.__str__()
print(tu)
