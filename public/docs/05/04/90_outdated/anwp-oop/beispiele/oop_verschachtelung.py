class Motor:
    def __init__(self, l, z, k):
        self.leistung = l
        self.zylinder = z
        self.kraftstoff = k
 
    def tunen(self, x):
        self.leistung += x
 
    def __str__(self):
        return f"{self.leistung} / {self.zylinder} / {self.kraftstoff}"

class Fahrzeug:
    def __init__(self, b, g, a):
        self.bezeichnung = b
        self.geschwindigkeit = g
        self.antrieb = a

    def __str__(self):
        return f"{self.bezeichnung} / {self.geschwindigkeit}," \
            f" Antrieb: {self.antrieb}"

ford = Fahrzeug("Ford Focus", 70, Motor(50, 4, "Diesel"))
ford.antrieb.tunen(10)
print(ford)
 
ford.antrieb.leistung = 80
ford.antrieb.zylinder = 6
ford.antrieb.kraftstoff = "Benzin"
print(ford)
