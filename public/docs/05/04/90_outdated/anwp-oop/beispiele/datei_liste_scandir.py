import os
eintrag_iterator = os.scandir(".")
for eintrag in eintrag_iterator:
    if eintrag.name.startswith("schr") and eintrag.name.endswith(".py"):
        try:
            d = open(eintrag)
        except:
            print("Datei nicht geöffnet")
            continue

        gesamtertext = d.read()
        d.close()
        if gesamtertext.find("Schmitz") != -1:
            print(eintrag.name)
eintrag_iterator.close()
