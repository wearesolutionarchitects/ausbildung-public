import tkinter

def ausgabe():
    lbAusgabe["text"] = liAuswahl.get("active")

def ende():
    fenster.destroy()

fenster = tkinter.Tk()
fenster.title("Einfach")
fenster.resizable(0, 0)

lbAuswahl = tkinter.Label(fenster, text="Ihre Auswahl:")
lbAuswahl.grid(row=0, column=0, sticky="w", padx=5, pady=5)

frAuswahl = tkinter.Frame(fenster)
frAuswahl.grid(row=1, column=0, padx=5, pady=5)

sbAuswahl = tkinter.Scrollbar(frAuswahl, orient="vertical")
liAuswahl = tkinter.Listbox(frAuswahl, height=4, yscrollcommand=sbAuswahl.set)
sbAuswahl["command"] = liAuswahl.yview

stadt = ["Hamburg", "Stuttgart", "Berlin", "Dortmund", "Trier",
         "Duisburg", "Potsdam", "Halle", "Flensburg", "Augsburg"]
for s in stadt:
    liAuswahl.insert("end", s)
liAuswahl.grid(row=0, column=0)
sbAuswahl.grid(row=0, column=1, sticky="sn")

buAusgabe = tkinter.Button(fenster, text="Ausgabe", command=ausgabe, width=10)
buAusgabe.grid(row=2, column=0, sticky="w", padx=5, pady=5)

lbAusgabe = tkinter.Label(fenster, text="(leer)")
lbAusgabe.grid(row=3, column=0, sticky="w", padx=5, pady=5)

buEnde = tkinter.Button(fenster, text="Ende", command=ende, width=10)
buEnde.grid(row=4, column=2, padx=5, pady=5)

fenster.mainloop()
