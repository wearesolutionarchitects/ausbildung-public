import tkinter

def auswahl():
    lbAusgabe["text"] = "Auswahl: " + farbe.get()

def ausgabe():
    lbAusgabe["text"] = "Ausgabe: " + farbe.get()

def ende():
    fenster.destroy()

fenster = tkinter.Tk()
fenster.title("Radiobuttons")
fenster.resizable(0, 0)

lbAuswahl = tkinter.Label(fenster, text="Farbe:", anchor="w", width=20)
lbAuswahl.grid(row=0, column=0, sticky="w", padx=5, pady=5)

farbe = tkinter.StringVar()
farbe.set("Rot")

frFarbe = tkinter.Frame(fenster)
frFarbe.grid(row=1, column=0, padx=5, pady=5)

rbRot = tkinter.Radiobutton(frFarbe, text="Rot", variable=farbe,
    value="Rot", command=auswahl)
rbRot.grid(row=0, column=0, padx=5, pady=5)

rbGelb = tkinter.Radiobutton(frFarbe, text="Gelb", variable=farbe,
    value="Gelb", command=auswahl)
rbGelb.grid(row=0, column=1, padx=5, pady=5)

rbBlau = tkinter.Radiobutton(frFarbe, text="Blau", variable=farbe,
    value="Blau", command=auswahl)
rbBlau.grid(row=0, column=2, padx=5, pady=5)

buAusgabe = tkinter.Button(fenster, text="Ausgabe", command=ausgabe, width=10)
buAusgabe.grid(row=2, column=0, sticky="w", padx=5, pady=5)

lbAusgabe = tkinter.Label(fenster, text="(leer)")
lbAusgabe.grid(row=3, column=0, sticky="w", padx=5, pady=5)

buEnde = tkinter.Button(fenster, text="Ende", command=ende, width=10)
buEnde.grid(row=4, column=1, padx=5, pady=5)

fenster.mainloop()
