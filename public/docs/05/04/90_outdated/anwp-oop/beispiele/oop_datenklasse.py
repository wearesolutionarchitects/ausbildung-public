import dataclasses, math
@dataclasses.dataclass
class Vektor:
    x:float = 0.0
    y:float = 0.0

    def betrag(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

va = Vektor(3.0, 4.0)
print(va)
print("Betrag:", va.betrag())

vb = Vektor(3.0, 4.0)
print(vb)

if va == vb:
    print("Vektoren sind gleich")

vc = Vektor(1.8)
print(vc)

vd = Vektor(y=9.1)
print(vd)

