import sys
def leseCode():
    try:
        d = open("morsen.txt")
    except:
        print("Datei nicht geöffnet")
        sys.exit(0)
    allezeilen = d.readlines()
    d.close()
    code = {}
    for zeile in allezeilen:
        worte = zeile.split()
        code[worte[0]] = worte[1]
    for i in range(97,123):
        code[chr(i)] = code[chr(i-32)]
    return code
