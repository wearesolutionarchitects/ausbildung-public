import sys
try:
    d = open("formatiert.txt","w")
except:
    print("Datei nicht geöffnet")
    sys.exit(0)

li = [["Maier", "Hans", 6714, 3500, "15.03.1962"], 
      ["Schmitz","Peter", 81343, 3750, "12.04.1958"], 
      ["Mertens", "Julia", 2297, 3621.5, "30.12.1959"]]
for ds in li:
    d.write(f"{ds[0]:12}{ds[1]:12}{ds[2]:6}{ds[3]:8.2f}{ds[4]:>11}\n")
d.close()
