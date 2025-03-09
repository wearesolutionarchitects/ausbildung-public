import sys
print("Parameter:", sys.argv)
print("Anzahl:", len(sys.argv))
 
summe = 0
for p in sys.argv[1:]:
    try:
        summe += float(p)
    except:
        print(f"Fehler bei Parameter {p}")
print("Summe:", summe)
