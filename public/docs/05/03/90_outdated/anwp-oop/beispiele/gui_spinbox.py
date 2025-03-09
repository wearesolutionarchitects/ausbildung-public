import tkinter.ttk

def auswahlStadt():
    lbAusgabe["text"] = "Auswahl: " + spStadt.get()

def auswahlZahl():
    lbAusgabe["text"] = "Auswahl: " + spZahl.get()

def ausgabe():
    lbAusgabe["text"] = f"Ausgabe: {spStadt.get()}/{spZahl.get()}"

def ende():
    fenster.destroy()

fenster = tkinter.Tk()
fenster.title("Spinbox")
fenster.resizable(0, 0)

lbAuswahl = tkinter.Label(fenster, text="Ihre Eingabe oder Auswahl:")
lbAuswahl.grid(row=0, column=0, padx=5, pady=5)

stadt = ["Hamburg", "Stuttgart", "Berlin", "Dortmund", "Trier",
         "Duisburg", "Potsdam", "Halle", "Flensburg", "Augsburg"]
spStadt = tkinter.ttk.Spinbox(fenster, values=stadt, command=auswahlStadt)
spStadt.set("Hamburg")
spStadt.grid(row=1, column=0, sticky="w", padx=5, pady=5)

spZahl = tkinter.ttk.Spinbox(fenster,
    from_=10, to=20, width=15, command=auswahlZahl)
spZahl.set(12)
spZahl.grid(row=2, column=0, sticky="w", padx=5, pady=5)

buAusgabe = tkinter.Button(fenster, text="Ausgabe", command=ausgabe, width=10)
buAusgabe.grid(row=3, column=0, sticky="w", padx=5, pady=5)

lbAusgabe = tkinter.Label(fenster, text="(leer)")
lbAusgabe.grid(row=4, column=0, sticky="w", padx=5, pady=5)

buEnde = tkinter.Button(fenster, text="Ende", command=ende, width=10)
buEnde.grid(row=5, column=3, sticky="w", padx=5, pady=5)

fenster.mainloop()
