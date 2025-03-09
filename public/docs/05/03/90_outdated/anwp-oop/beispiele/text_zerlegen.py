tx = "Das ist ein Satz"
print("Text:", tx)
liste = tx.split()
for i in range(0, len(liste)):
    print("Element:", i, liste[i])
print()

tx = "Maier;Hans;6714;3.500,00;15.03.62"
print("Text:", tx)
liste = tx.split(";")
for i in range(0, len(liste)):
    print("Element:", i, liste[i])
