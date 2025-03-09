z = [["Paris","Fr",3.5], ["Rom","It",4.2], ["Madrid","Sp",3.2]]
print("Liste:", z)
print("Länge:", len(z))
print()

print("Unter-Liste:", z[0])
print("Länge:", len(z[0]))
print("Slice von Unter-Listen:", z[:2])
print()

print("Element:", z[2][0])
print("Länge:", len(z[2][0]))
print("Slice von Elementen:", z[2][:2])
print("Slice auf der untersten Ebene:", z[2][0][:3])
print()

for i in range(len(z)):
    print(f"{i}: {z[i][0]} hat {z[i][2]} Mio. Einwohner")
for stadt in z:
    print(f"{stadt[0]} hat {stadt[2]} Mio. Einwohner")
