import tkinter

def verdoppeln():
    try:
        zahl = float(etEingabe.get())
        lbAusgabe["text"] = zahl * 2
    except:
        lbAusgabe["text"] = "Keine Zahl"

def ende():
    fenster.destroy()

fenster = tkinter.Tk()
fenster.title("Einzeilig")
fenster.resizable(0, 0)

lbEingabe = tkinter.Label(fenster, text="Ihre Eingabe:")
lbEingabe.grid(row=0, column=0, sticky="w", padx=5, pady=5)

etEingabe = tkinter.Entry(fenster)
etEingabe.grid(row=1, column=0, padx=5, pady=5)

buVerdoppeln = tkinter.Button(fenster, text="Verdoppeln",
    command=verdoppeln, width=10)
buVerdoppeln.grid(row=2, column=0, sticky="w", padx=5, pady=5)

lbAusgabe = tkinter.Label(fenster, text="(leer)")
lbAusgabe.grid(row=3, column=0, sticky="w", padx=5, pady=5)

buEnde = tkinter.Button(fenster, text="Ende", command=ende, width=10)
buEnde.grid(row=4, column=1, padx=5, pady=5)

fenster.mainloop()
