import tkinter

def pruefen():
    pw = etPasswort.get() 
    if pw == "Bingo":
        lbAusgabe["text"] = "Zugang erlaubt"
    else:
        lbAusgabe["text"] = "Zugang nicht erlaubt"
    etPasswort.delete(0, "end")
    buEnde["state"] = "normal"

def ende():
    fenster.destroy()

fenster = tkinter.Tk()
fenster.title("Passwort")
fenster.resizable(0, 0)

lbPasswort = tkinter.Label(fenster, text="Ihr Passwort:")
lbPasswort.grid(row=0, column=0, sticky="w", padx=5, pady=5)

etPasswort = tkinter.Entry(fenster, show="*")
etPasswort.grid(row=1, column=0, padx=5, pady=5)

buPruefen = tkinter.Button(fenster, text="Prüfen",
    command=pruefen, width=10)
buPruefen.grid(row=2, column=0, sticky="w", padx=5, pady=5)

lbAusgabe = tkinter.Label(fenster, text="(leer)")
lbAusgabe.grid(row=3, column=0, sticky="w", padx=5, pady=5)

buEnde = tkinter.Button(fenster, text="Ende", command=ende,
                        width=10, state="disabled")
buEnde.grid(row=4, column=1, padx=5, pady=5)

fenster.mainloop()
