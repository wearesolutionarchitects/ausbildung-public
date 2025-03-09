import tkinter

def schrift():
    for x in range(5, 94):
        for y in range(69, 80):
            imBild.put("#00549D", (x, y))

def transparent():
    for x in range(5, 94):
        for y in range(38, 46):
            imBild.transparency_set(x, y, True)
    if imBild.transparency_get(50, 40):
        print("Punkt ist transparent")

def ende():
    fenster.destroy()

fenster = tkinter.Tk()
fenster.title("Bild")
fenster.resizable(0, 0)

imBild = tkinter.PhotoImage(file="rheinwerk.png")
lbBild = tkinter.Label(fenster)
lbBild["image"] = imBild
lbBild.grid(row=0, column=0, padx=5, pady=5)

print("Breite:", imBild.width())
print("Höhe:", imBild.height())
print("Farbe x,y:", imBild.get(0, 0))
if not imBild.transparency_get(50, 40):
    print("Punkt ist nicht transparent")

buSchrift = tkinter.Button(fenster,
    text="Schrift in Blau", command=schrift, width=20)
buSchrift.grid(row=1, column=0, padx=5, pady=5)

buTransparent = tkinter.Button(fenster,
    text="Bereich transparent", command=transparent, width=20)
buTransparent.grid(row=2, column=0, padx=5, pady=5)

buEnde = tkinter.Button(fenster, text="Ende", command=ende, width=10)
buEnde.grid(row=3, column=1, padx=5, pady=5)

fenster.mainloop()
