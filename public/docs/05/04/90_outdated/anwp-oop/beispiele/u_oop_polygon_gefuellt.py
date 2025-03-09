from u_oop_geometrie import *

polygonGefuellt1 = PolygonGefuellt([Punkt(3.5, 1.0),
    Punkt(-2.0, 6.5), Punkt(1.5, -3.5)], "Rot")
print(polygonGefuellt1)
polygonGefuellt1.verschieben(0.5, 2.5)
print(polygonGefuellt1)
polygonGefuellt1.faerben("Blau")
print(polygonGefuellt1)
