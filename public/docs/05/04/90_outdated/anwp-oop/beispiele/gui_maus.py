import tkinter

def bewegt(e):
    lbAusgabe["text"] = f"x={e.x}, y={e.y}"

def links(e):
    lbAusgabe["text"] = "Links gedrückt"

def linkslos(e):
    lbAusgabe["text"] = "Links losgelassen"

def rechts(e):
    lbAusgabe["text"] = "Rechts gedrückt"

def rechtslos(e):
    lbAusgabe["text"] = "Rechts losgelassen"

def verlassen(e):
    lbAusgabe["text"] = "Verlassen"

def betreten(e):
    lbAusgabe["text"] = "Betreten"

def ende():
    fenster.destroy()

fenster = tkinter.Tk()
fenster.title("Maus")
fenster.resizable(0, 0)

imBild = tkinter.PhotoImage(file="rheinwerk.png")
lbBild = tkinter.Label(fenster, image=imBild)
lbBild.bind("<Motion>", bewegt)
lbBild.bind("<Button 1>", links)
lbBild.bind("<ButtonRelease 1>", linkslos)
lbBild.bind("<Button 3>", rechts)
lbBild.bind("<ButtonRelease 3>", rechtslos)
lbBild.bind("<Leave>", verlassen)
lbBild.grid(row=0, column=0, padx=5, pady=5)

lbAusgabe = tkinter.Label(fenster, text="(leer)")
lbAusgabe.grid(row=1, column=0, sticky="w", padx=5, pady=5)

buEnde = tkinter.Button(fenster, text="Ende", command=ende, width=10)
buEnde.grid(row=2, column=1, padx=5, pady=5)
buEnde.bind("<Enter>", betreten)

fenster.mainloop()


