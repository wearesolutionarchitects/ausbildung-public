zahl = 2


def manipulation(input_zahl):
  print("input_zahl",input_zahl)
  print("ID-input_zahl",id(input_zahl))
  input_zahl = 4
  print("ID-input_zahl nach Zuweisung", id(input_zahl))

  return input_zahl

print("ID von zahl",id(zahl))
print("ID Funktionsaufruf",id(manipulation(zahl))) # call by value
print(id(zahl))
print(zahl)
