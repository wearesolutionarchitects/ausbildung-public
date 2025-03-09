liste = [1,2,3] # global, Liste, mutable

i = 5.7 # Integer, immutable


def manipulation(input_liste,input_i:int): # Parameter inpu_liste, lokal

  input_i = 10000
  #input_liste = [] # neue Liste
  input_liste_2 = input_liste
  input_liste_2.append(100)
  #print(input_i) # hier wird 7 auf den Bildschirm geschrieben
  input_liste.append(8)
  #print(id(input_liste))
  return input_liste,input_i

#print(id(liste))
manipulation(liste,i) # Funktionsaufruf mit Argument liste


print(liste) #mutable
print(i) #immutable