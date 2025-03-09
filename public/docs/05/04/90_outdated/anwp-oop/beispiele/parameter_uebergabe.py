def aendern(za, tx, li, di, st):
    za = 8
    tx = "ciao "
    li[0] = 7
    di["x"] = 7
    st.discard(3)
    print(f"Funktion: {za} {tx} {li} {di} {st}")

hza = 3
htx = "hallo"
hli = [3,"abc"]
hdi = {"x":3, "y":"abc"}
hst = set([3, "abc"])

print(f"Vorher:   {hza} {htx} {hli} {hdi} {hst}")
aendern(hza, htx, hli, hdi, hst)
print(f"Nachher:  {hza} {htx} {hli} {hdi} {hst}")
