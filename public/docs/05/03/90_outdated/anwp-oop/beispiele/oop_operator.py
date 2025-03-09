import math

class Bruch:
    def __init__(self, zaehler=1, nenner=1):
        self.z = zaehler
        self.n = nenner if nenner != 0 else 1
    def kuerzen(self):
        g = math.gcd(self.z, self.n)
        self.z = int(self.z / g)
        self.n = int(self.n / g)
        if self.n < 0:
            self.z *= -1
            self.n *= -1
    def wert(self):
        return self.z / self.n
    def __str__(self):
        self.kuerzen()
        return f"{self.z}/{self.n}" if self.n != 1 else f"{self.z}"
    def __mul__(self, anderer):
        return Bruch(self.z * anderer.z, self.n * anderer.n)
    def __truediv__(self, anderer):
        return Bruch(self.z * anderer.n, self.n * anderer.z)
    def __add__(self, anderer):
        return Bruch(self.z * anderer.n + self.n * anderer.z,
                     self.n * anderer.n)
    def __sub__(self, anderer):
        return Bruch(self.z * anderer.n - self.n * anderer.z,
                     self.n * anderer.n)
    def __eq__(self, anderer):
        self.kuerzen()
        anderer.kuerzen()
        return self.z == anderer.z and self.n == anderer.n
    def __gt__(self, anderer):
        return self.wert() > anderer.wert()
    def __lt__(self, anderer):
        return self.wert() < anderer.wert()

b1 = Bruch(3, -2)
b2 = Bruch(1, 4)

b3 = b1 * b2
print(f"{b1} * {b2} = {b3}")
print(f"{b1} / {b2} = {b1 / b2}")
print(f"{b1} + {b2} = {b1 + b2}")
print(f"{b1} - {b2} = {b1 - b2}")
print(f"{b1} + {b2} * {b3}= {b1 + b2 * b3}")
print(f"({b1} + {b2}) * {b3}= {(b1 + b2) * b3}")

b4 = Bruch(-30, 20)
print(f"{b1} == {b4}: {b1 == b4}")
print(f"{b2} > {b4}: {b2 > b4}")
print(f"{b2} < {b4}: {b2 < b4}")

