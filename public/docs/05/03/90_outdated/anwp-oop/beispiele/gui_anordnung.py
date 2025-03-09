import tkinter

def hallo():
    lbAusgabe["text"] = "Hallo"

def ende():
    fenster.destroy()

fenster = tkinter.Tk()
fenster.title("GUI")
fenster.resizable(0, 0)

buHallo = tkinter.Button(fenster, text="Hallo", command=hallo, width=10)
buHallo.grid(row=0, column=0, sticky="w", padx=5, pady=5)

lbAusgabe = tkinter.Label(fenster, text="(leer)",
    anchor="w", relief="sunken", width=20)
lbAusgabe.grid(row=1, column=0, padx=5, pady=5)

buEnde = tkinter.Button(fenster, text="Ende", command=ende, width=10)
buEnde.grid(row=2, column=1, padx=5, pady=5)

fenster.mainloop()
