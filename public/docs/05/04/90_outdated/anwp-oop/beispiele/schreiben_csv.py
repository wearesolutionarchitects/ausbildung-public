import sys
try:
    d = open("daten.csv","w")
except:
    print("Datei nicht geöffnet")
    sys.exit(0)

li = [["Maier", "Hans", 6714, 3500, "15.03.1962"], 
      ["Schmitz","Peter", 81343, 3750, "12.04.1958"], 
      ["Mertens", "Julia", 2297, 3621.5, "30.12.1959"]]
for ds in li:
    gh = str(ds[3]).replace('.',',')
    d.write(f"{ds[0]};{ds[1]};{ds[2]};{gh};{ds[4]}\n")
d.close()
