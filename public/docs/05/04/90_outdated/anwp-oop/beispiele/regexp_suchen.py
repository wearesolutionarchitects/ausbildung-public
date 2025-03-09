import re

tx = "Haus und Maus und Laus"
print(tx)
print("1:", re.findall("Maus",tx))
print("2:", re.findall("[HM]aus",tx))
print("3:", re.findall("[L-M]aus",tx))
print("4:", re.findall("[^L-M]aus",tx))
print("5:", re.findall(".aus",tx))
print("6:", re.findall("^.aus",tx))
print("7:", re.findall(".aus$",tx))
print()

tx = "0172-445633"
print(tx)
print("8:", re.findall("[0-2]",tx))
print("9:", re.findall("[^0-2]",tx))
print("10:", re.findall("[047-]",tx))
print()

tx = "aa und aba und abba und abbba und aca"
print(tx)
print("11:", re.findall("ab*a",tx))
print("12:", re.findall("ab+a",tx))
print("13:", re.findall("ab?a",tx))
print("14:", re.findall("ab{2,3}a",tx))
print()
