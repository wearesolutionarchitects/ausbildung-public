tx = "Das ist ein Beispielsatz"
print("Text:", tx)

such = "ei"
print("Suchtext:", such)
print()

anz = tx.count(such)
print(f"count: Der String {such} kommt {anz} mal vor")

pos = tx.find(such)
while pos != -1:
    print("An Position", pos)
    pos = tx.find(such, pos+1)

pos = tx.rfind(such)
if pos != -1:
    print("rfind: Zum letzten Mal an Position", pos)
print()

if tx.startswith("Das"):
    print("Text beginnt mit Das")
if not tx.endswith("Das"):
    print("Text endet nicht mit Das")

tx = tx.replace("ist", "war")
print("Nach Ersetzen:", tx)

z = 48.2
tx = str(z)
tx = tx.replace(".", ",")
print("Zahl mit Komma:", tx)
