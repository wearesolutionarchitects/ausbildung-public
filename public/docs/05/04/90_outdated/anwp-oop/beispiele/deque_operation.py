import collections
 
d1 = collections.deque([8, 18, 28])
print("Erstellt:", d1)
d2 = d1.copy()
print("Kopie:", d2)
 
print("Elemente:")
for x in d1:
    print(x)
for i in range(len(d1)):
    print(f"{i}: {d1[i]}")
 
d3 = d1 * 2
print("Deque verdoppelt:", d3)
d4 = collections.deque([9, 19, 29])
d5 = d1 + d4
print("Andere deque addiert:", d5)
 
d1.clear()
print("Nach Leerung:", d1)
