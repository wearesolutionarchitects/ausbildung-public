import random, time
 
random.seed()
richtig = 0
startzeit = time.time()
 
for aufgabe in range(5):
    a = random.randint(10,30)
    b = random.randint(10,30)
    c = a + b
    print(f"Aufgabe {aufgabe+1} von 5: {a} + {b}")
    try:
        zahl = int(input("Bitte Lösungsvorschlag eingeben: "))
        if zahl == c:
            print("Richtig")
            richtig += 1
        else:
            raise
    except:
        print("Falsch")
 
differenz = time.time() - startzeit
print(f"Richtig: {richtig} von 5 in {differenz:.2f} Sekunden")
print("Ergebnis erzielt:", time.strftime("%d.%m.%Y %H:%M:%S"))
