import tkinter

def auswahl():
    lbAusgabe["text"] = f"Auswahl: {dusche.get()}, {minibar.get()}"

def ausgabe():
    lbAusgabe["text"] = f"Ausgabe: {dusche.get()}, {minibar.get()}"

def ende():
    fenster.destroy()

fenster = tkinter.Tk()
fenster.title("Checkbuttons")
fenster.resizable(0, 0)

lbAuswahl = tkinter.Label(fenster, text="Zimmer:", anchor="w", width=30)
lbAuswahl.grid(row=0, column=0, padx=5, pady=5)

dusche = tkinter.StringVar()
dusche.set("ohne Dusche")

minibar = tkinter.StringVar()
minibar.set("ohne Minibar")

ckDusche = tkinter.Checkbutton(fenster, text="Dusche", variable=dusche,
    onvalue="mit Dusche", offvalue="ohne Dusche", command=auswahl)
ckDusche.grid(row=1, column=0, sticky="w", padx=5, pady=5)

ckMinibar = tkinter.Checkbutton(fenster, text="Minibar", variable=minibar,
    onvalue="mit Minibar", offvalue="ohne Minibar", command=auswahl)
ckMinibar.grid(row=2, column=0, sticky="w", padx=5, pady=5)

buAusgabe = tkinter.Button(fenster, text="Ausgabe",
    command=ausgabe, width=10)
buAusgabe.grid(row=3, column=0, sticky="w", padx=5, pady=5)

lbAusgabe = tkinter.Label(fenster, text="(leer)")
lbAusgabe.grid(row=4, column=0, sticky="w", padx=5, pady=5)

buEnde = tkinter.Button(fenster, text="Ende", command=ende, width=10)
buEnde.grid(row=5, column=2, padx=5, pady=5)

fenster.mainloop()
