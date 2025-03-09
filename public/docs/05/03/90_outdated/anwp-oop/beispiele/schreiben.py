import sys

try:
    d = open("schreiben.txt","w")
except:
    print("Datei nicht geöffnet")
    sys.exit(0)

d.write("Die erste Zeile\n")
for i in range(2,11,2):
    d.write(f"{i} ")
d.write("\n")

li = ["Hamburg", "Berlin", "München"]
d.writelines(li)
d.write("\n")
for i in li:
    d.write(f"{i}\n")

dc = {"Peter":31, "Julia":28, "Werner":35}
d.writelines(dc)
d.write("\n")
for k,v in dc.items():
    d.write(f"{k}:{v}\n")

d.close()
