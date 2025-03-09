import os

filename = os.path.join(os.path.dirname(__file__), "ordner", "..", "ordner", "unterordner", "datei.txt")
with open(filename, "r") as file:
    for line in file:
        print(line)

#folder = os.path.join(os.path.dirname(__file__), "ordner")
#
#for file in os.listdir(folder):
#    file_path = os.path.join(folder, file)
#    if os.path.isdir(file_path):
#        print(file + " ist ein Ordner")
#    else:
#        print(file + " ist eine Datei")

