import random, time, glob, pickle

def hs_lesen():
    global hs_liste
    if not glob.glob("highscore.bin"):
        hs_liste = []
        return
    d = open("highscore.bin", "rb")
    hs_liste = pickle.load(d)
    d.close()

def hs_anzeigen():
    if not hs_liste:
        print("Keine Highscores vorhanden")
        return
    print(" P. Name            Zeit")
    for i in range(len(hs_liste)):
        print(f"{i+1:2d}. {hs_liste[i][0]:10} {hs_liste[i][1]:5.2f} sec")
        if i >= 9:
            break

def hs_schreiben():
    d = open("highscore.bin","wb")
    pickle.dump(hs_liste,d)
    d.close()

def spiel():
    name = input("Bitte geben Sie Ihren Namen ein (max. 10 Zeichen): ")
    name = name[:10]
    richtig = 0
    startzeit = time.time()

    for aufgabe in range(5):
        a = random.randint(10,30)
        b = random.randint(10,30)
        c = a + b

        try:
            zahl = int(input(f"Aufgabe {aufgabe+1} von 5: {a} + {b} : "))
            if zahl == c:
                print("*** Richtig ***")
                richtig += 1
            else:
                raise
        except:
            print("* Falsch *")

    differenz = time.time() - startzeit
    print(f"Ergebnis: {richtig:d} von 5 in {differenz:.2f} Sekunden", end = "")
    if richtig == 5:
        print(", Highscore")
    else:
        print(", leider kein Highscore")
        return

    gefunden = False
    for i in range(len(hs_liste)):
        if differenz < hs_liste[i][1]:
            hs_liste.insert(i, [name, differenz])
            gefunden = True
            break
    if not gefunden:
        hs_liste.append([name, differenz])
    hs_anzeigen()

# Programm
random.seed()
hs_lesen()

while True:
    try:
        menu = int(input("Bitte eingeben "
            "(0: Ende, 1: Highscores, 2: Spielen): "))
    except:
        print("Falsche Eingabe")
        continue

    if menu == 0:
        break
    elif menu == 1:
        hs_anzeigen()
    elif menu == 2:
        spiel()
    else:
        print("Falsche Eingabe")

hs_schreiben()
