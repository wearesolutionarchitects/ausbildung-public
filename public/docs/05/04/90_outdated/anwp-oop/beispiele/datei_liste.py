import glob
dateiliste = glob.glob("schr*.py")
for datei in dateiliste:
    try:
        d = open(datei)
    except:
        print("Datei nicht geöffnet")
        continue
    gesamtertext = d.read()
    d.close()
    if gesamtertext.find("Schmitz") != -1:
        print(datei)
