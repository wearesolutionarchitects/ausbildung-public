import datetime

d1 = datetime.timedelta(5)
print("Nur Tage:", d1)

d2 = datetime.timedelta(5, 8, 0, 0, 10, 2, 1)
print("Alle Parameter:", d2)

d3 = datetime.timedelta(days=1, hours=30, minutes=-20, seconds=80)
print("Benannte Parameter, Umrechnung:", d3)
print(f"Eigenschaften: {d3.days} Tage, {d3.seconds} Sekunden")

sk = d3.total_seconds()
mi = sk / 60
st = mi / 60
print(f"Methode, Umrechnung: {sk:.0f} Sek. = {mi:.3f} Min. = {st:.3f} Std.")
print()

print("Operatoren:")
a = datetime.timedelta(days=5, hours=10)
print("Zeitdifferenz a:", a)
b = datetime.timedelta(days=2, hours=4)
print("Zeitdifferenz b:", b)

print("a + b:", a + b)
print("a - b:", a - b)
print("b * 2.5:", b * 2.5)
print("a / 2:", a / 2)
print("a / b:", a / b)
print("a % b:", a % b)
print("a == b:", a == b)
print("a > b:", a > b)
