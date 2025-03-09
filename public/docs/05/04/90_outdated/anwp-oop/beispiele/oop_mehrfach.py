class Datum:
    def __init__(self, d, m, y):
        self.tag = d
        self.monat = m
        self.jahr = y
    def __str__(self):
        return f"{self.tag:02d}.{self.monat:02d}.{self.jahr:d}"
 
class Uhrzeit:
    def __init__(self, h, m, s):
        self.stunde = h
        self.minute = m
        self.sekunde = s
    def __str__(self):
        return f"{self.stunde:02d}:{self.minute:02d}:{self.sekunde:02d}"
 
class Zeit(Datum, Uhrzeit):
    def __init__(self, d, mo, y, h, mi, s):
        Datum.__init__(self, d, mo, y)
        Uhrzeit.__init__(self, h, mi, s)
    def __str__(self):
        return f"{Datum.__str__(self)} {Uhrzeit.__str__(self)}"
 
d = Datum(12, 8, 2024)
print(d)
u = Uhrzeit(16, 5, 20)
print(u)
z = Zeit(5, 11, 2024, 9, 35, 8)
print(z)
