class Punkt:
    def __init__(self, xk=0.0, yk=0.0):
        self.x = xk
        self.y = yk
    def verschieben(self, dx, dy):
        self.x += dx
        self.y += dy
    def __str__(self):
        return f"({self.x} / {self.y})"

class Linie:
    def __init__(self, b=Punkt(), e=Punkt()):
        self.beginn = b
        self.ende = e
    def verschieben(self, dx, dy):
        self.beginn.verschieben(dx, dy)
        self.ende.verschieben(dx, dy)
    def __str__(self):
        return f"{self.beginn} / {self.ende}"

class Polygon:
    def __init__(self, p=[]):
        self.punkte = p

    def verschieben(self, dx, dy):
        for p in self.punkte:
            p.verschieben(dx, dy)

    def __str__(self):
        if len(self.punkte) == 0:
            return "(Keine Punkte)"

        ausgabe = ""
        for i in range(len(self.punkte)):
            ausgabe += str(self.punkte[i])
            if i < len(self.punkte) - 1:
                ausgabe += " / "
        return ausgabe

class PolygonGefuellt(Polygon):
    def __init__(self, p=[], f=""):
        super().__init__(p)
        self.farbe = f
    def faerben(self, f):
        self.farbe = f
    def __str__(self):
        return f"{super().__str__()} {self.farbe}"
