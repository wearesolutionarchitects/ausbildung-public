import sys, shutil, os, glob
print(glob.glob("le*.txt"))

if not os.path.exists("lesen.txt"):
    print("Datei nicht vorhanden")
    sys.exit(0)

shutil.copy("lesen.txt","lesen_kopie.txt")
print(glob.glob("le*.txt"))

try:
    shutil.move("lesen_kopie.txt","lesen_neu.txt")
except:
    print("Fehler beim Umbenennen")
print(glob.glob("le*.txt"))

try:
    os.remove("lesen_neu.txt")
except:
    print("Fehler beim Entfernen")
print(glob.glob("le*.txt"))
