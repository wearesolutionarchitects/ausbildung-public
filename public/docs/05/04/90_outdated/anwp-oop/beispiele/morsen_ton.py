import sys, morsen, time, winsound
def tonCode(text, code):
    signalDauer = {".":200, "-":600}
    signalPause = 0.2
    zeichenPause = 0.6
    wortPause = 1.4

    alleWorte = text.split()
    for w in range(len(alleWorte)):
        wort = alleWorte[w]
        for z in range(len(wort)):
            zeichen = wort[z]
            print(zeichen, end="")
            try:
                alleSignale = code[zeichen]
                for s in range(len(alleSignale)):
                    signal = alleSignale[s]
                    winsound.Beep(800, signalDauer[signal])
                    if s < len(alleSignale)-1:
                        time.sleep(signalPause)
                if z < len(wort)-1:
                    time.sleep(zeichenPause)
            except KeyError:
                pass
        if w < len(alleWorte)-1:
            print(" ", end="")
            time.sleep(wortPause)

code = morsen.leseCode()
tonCode("Hallo Welt", code)
