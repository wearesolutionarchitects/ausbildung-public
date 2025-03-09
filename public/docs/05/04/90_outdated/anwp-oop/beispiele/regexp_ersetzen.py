import re

tx = "Haus und Maus und Laus"
print(tx)
print("1:", re.sub("Maus","x",tx))
print("2:", re.sub("[H|M]aus","x",tx))
print("3:", re.sub("[L-M]aus","x",tx))
print("4:", re.sub("[^L-M]aus","x",tx))
print("5:", re.sub(".aus","x",tx))
print("6:", re.sub("^.aus","x",tx))
print("7:", re.sub(".aus$","x",tx))
print()

tx = "0172-445633"
print(tx)
print("8:", re.sub("[0-2]","x",tx))
print("9:", re.sub("[^0-2]","x",tx))
print("10:", re.sub("[047-]","x",tx))
print()

tx = "aa und aba und abba und abbba und aca"
print(tx)
print("11:", re.sub("ab*a","x",tx))
print("12:", re.sub("ab+a","x",tx))
print("13:", re.sub("ab?a","x",tx))
print("14:", re.sub("ab{2,3}a","x",tx))
