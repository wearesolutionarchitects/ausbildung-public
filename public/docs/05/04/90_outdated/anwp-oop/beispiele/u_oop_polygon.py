from u_oop_geometrie import *

polygon1 = Polygon()
print(polygon1)
punkt1 = Punkt(3.5, 2.5)
punkt2 = Punkt(-2.0, 8.5)
polygon2 = Polygon([punkt1, Punkt(3.0), punkt2])
print(polygon2)
polygon2.verschieben(1.0, 2.5)
print(polygon2)
