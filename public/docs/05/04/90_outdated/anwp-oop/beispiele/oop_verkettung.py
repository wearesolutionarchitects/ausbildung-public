class Rechteck:
    def __init__(self, f, x, y, b, h):
        self.farbe = f
        self.xpos = x
        self.ypos = y
        self.breite = b
        self.hoehe = h
    def __str__(self):
        return f"Farbe: {self.farbe}, Ort: {self.xpos}/{self.ypos}" \
               f", Größe: {int(self.breite)}/{int(self.hoehe)}"
    def faerben(self, f):
        self.farbe = f
        return self
    def verschieben(self, xDelta, yDelta):
        self.xpos += xDelta
        self.ypos += yDelta
        return self
    def skalieren(self, xFaktor, yFaktor):
        self.breite *= xFaktor
        self.hoehe *= yFaktor
        return self

r = Rechteck("Blau", 50, 10, 30, 50)
print(r)

r.faerben("Gelb")
r.verschieben(20, 50)
r.skalieren(2, 2.5)
print(r)

r.faerben("Blau").verschieben(-20, -50).skalieren(0.5, 0.4)
print(r)
