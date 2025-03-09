import math
def kreis(radius):
    flaeche = math.pi * radius * radius
    umfang = 2 * math.pi * radius
    return flaeche, umfang

f, u = kreis(3)
print(f"Fläche: {f:.3f}, Umfang: {u:.3f}")
x = kreis(3)
print(f"Fläche: {x[0]:.3f}, Umfang: {x[1]:.3f}")
