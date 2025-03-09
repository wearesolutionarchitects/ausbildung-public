import os, time
info = os.stat("formatiert.txt")
print("Größe in Byte:", info.st_size)
aus = "%d.%m.%Y %H:%M:%S"
print("Letzter Zugriff:", time.strftime(aus, time.localtime(info.st_atime)))
print("Letzte Modifikation:", time.strftime(aus, time.localtime(info.st_mtime)))
print("Erste Erstellung:", time.strftime(aus, time.localtime(info.st_birthtime)))
