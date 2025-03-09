import random

def zahl():
    zufallsnummer = random.randint(1, 300)
    attempts = 0

    print("Willkommen zum Zahlraten-Spiel!")
    print("Versuche die Zahl zwischen 1 und 300 zu erraten.")

    while True:
        benutzereingabe = int(input("Gib eine Zahl ein: "))
        attempts += 1

        if benutzereingabe < zufallsnummer:
            print("Die gesuchte Zahl ist höher.")
        elif benutzereingabe > zufallsnummer:
            print("Die gesuchte Zahl ist niedriger.")
        else:
            print(f"Glückwunsch! Du hast die richtige Zahl {zufallsnummer} in {attempts} Versuchen erraten!")
            break

    print(f"Du hast die Zahl in insgesamt {attempts} Versuchen erraten.")

zahl()