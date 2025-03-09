import tkinter, tkinter.scrolledtext

def laden():
    txText.delete(1.0, "end")
    try:
        d = open("gui_mehrzeilig.txt")
        txText.insert(1.0, d.read())
        d.close()
    except:
        txText.insert(1.0, "Datei nicht geöffnet")

def speichern():
    try:
        d = open("gui_mehrzeilig.txt", "w")
        d.write(txText.get(1.0, "end"))
        d.close()
    except:
        txText.insert(1.0, "Datei nicht geöffnet")

def loeschen():
    txText.delete(1.0, "end")

def ende():
    fenster.destroy()

fenster = tkinter.Tk()
fenster.title("Mehrzeilig")
fenster.resizable(0, 0)

lbText = tkinter.Label(fenster, text="Text:")
lbText.grid(row=0, column=0, sticky="w", padx=5, pady=5)

txText = tkinter.scrolledtext.ScrolledText(fenster, width=50, height=4)
txText.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

buLaden = tkinter.Button(
    fenster, text="Aus Datei laden", command=laden, width=15)
buLaden.grid(row=2, column=0, sticky="w", padx=5, pady=5)

buSpeichern = tkinter.Button(
    fenster, text="In Datei speichern", command=speichern, width=15)
buSpeichern.grid(row=2, column=1, padx=5, pady=5)

buLoeschen = tkinter.Button(
    fenster, text="Text löschen", command=loeschen, width=15)
buLoeschen.grid(row=2, column=2, sticky="e", padx=5, pady=5)

buEnde = tkinter.Button(fenster, text="Ende", command=ende, width=10)
buEnde.grid(row=3, column=3, padx=5, pady=5)

fenster.mainloop()

