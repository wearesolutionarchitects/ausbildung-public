import random, math
random.seed

prob = 2, 2, 2, 2, 3, 3, 3, 5, 5, 7
ops = "+", "-", "*", "/"

def produkt(anzahl):
    wert = 1
    for i in range(anzahl):
        wert *= random.choice(prob)
    if random.randint(0,1) == 0:
        return wert
    else:
        return -wert

def ausgabe(z, n):
    ggT = math.gcd(z, n)
    z = int(z / ggT)
    n = int(n / ggT)
    if n < 0:
        z *= -1
        n *= -1
    print("Ergebnis:", z if n == 1 else f"{z}/{n}")
    
def leicht():
    faktor = random.randint(-10, 10)
    n = 0
    while n == 0:
        n = random.randint(-10, 10)
    z = faktor * n
    print(f"Ganze Zahl berechnen: {z}/{n}")
    input()
    print("Ergebnis:", faktor)

def mittel():
    z = produkt(3)
    n = produkt(3)
    print(f"Bruch kürzen: {z}/{n}")
    input()
    ausgabe(z, n)
    
def schwer():
    az = produkt(2)
    an = produkt(2)
    bz = produkt(2)
    bn = produkt(2)
    op = random.choice(ops)
    print(f"Ergebnisbruch berechnen: {az}/{an} {op} {bz}/{bn}")

    if op == "+":
        z = az * bn + an * bz
        n = an * bn
    elif op == "-":
        z = az * bn - an * bz
        n = an * bn
    elif op == "*":
        z = az * bz
        n = an * bn
    else:
        z = az * bn
        n = an * bz

    input()
    ausgabe(z, n)
    
# Programm
while True:
    while True:
        print("Ihre Wahl: 1 = Leicht, 2 = Mittel, 3 = Schwer, 0 = Ende")
        try:
            wahl = int(input())
            if wahl < 0 or wahl > 3:
                raise
            else:
                break
        except:
            print("Bitte nur 0, 1, 2 oder 3 eingeben")

    if wahl == 0:
        break
    elif wahl == 1:
        leicht()
    elif wahl == 2:
        mittel()
    else:
        schwer()

