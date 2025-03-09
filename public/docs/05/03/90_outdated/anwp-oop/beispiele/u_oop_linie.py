from u_oop_geometrie import *

linie1 = Linie()
print(linie1)
punkt1 = Punkt(3.5, 2.5)
linie2 = Linie(Punkt(1.5, 4.0), punkt1)
print(linie2)
linie3 = Linie(Punkt(-2, 5.5))
print(linie3)
linie4 = Linie(e=Punkt(2.5, 1.0))
print(linie4)
linie4.verschieben(-2.0, 1.5)
print(linie4)

