st = set([8, 5, 5, 2, 5])
print("Set:", st)
print("Anzahl:", len(st))

for x in st:
    print(x)
if 5 in st:
    print("Wert ist enthalten")

su = set([2, 8])
if su < st:
    print("Echte Teilmenge")
sv = set([2, 8, 5])
if sv <= st:
    print("Teilmenge")

st.add(-12)
st.add(-12)
print("Element hinzu:", st)

st.discard(5)
print("Element entfernt:", st)

sk = st.copy()
print("Kopie:", sk)

sk.clear()
print("Geleert:", sk)

sf = frozenset([8, 5, 5, 2, 5])
print("Frozenset:", sf)
