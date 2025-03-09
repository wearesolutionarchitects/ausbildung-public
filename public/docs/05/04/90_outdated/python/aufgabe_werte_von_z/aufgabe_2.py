# Thema: Werte von z

# Aufhabe: 2.1
z = 0
while i in range (1,4):
    z = z * i
    print(z)

# Aufgabe 2.2
z = 2
i = 99
while i > 88:
    z = z + 3
    z = -z
    i = i - 2
print(z)

# Aufgabe 2.3
i = 0
z = 0
while i < 20:
    j = i
    while j < 20:
        z = z + j
        j = j + 1
        i = i + 5
print(z)

# Aufgabe 2.4
z = 4
i = 4
while i > 0:
    z = z + 4
    z = z / i
    i = i - 1
print(z)

# Aufgabe 2.5
z = 0
while z not in [1, 2]:
    z = int(input("Bitte geben Sie eine Zahl ein: "))
print("Programm beendet.")
