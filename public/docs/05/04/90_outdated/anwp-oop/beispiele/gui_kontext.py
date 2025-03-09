import tkinter

def zeigeKontext(e):
    mKontext.tk_popup(e.x_root, e.y_root)

def farbwechsel():
    lbHallo["bg"] = farbe.get()

def ende():
    fenster.destroy()  

fenster = tkinter.Tk()
fenster.title("Kontextmenü")
fenster.resizable(0, 0)

lbHallo = tkinter.Label(fenster, text="Hallo", width=20, bg="#FAAC58")
lbHallo.bind("<Button 3>", zeigeKontext)
lbHallo.grid(row=0, column=0, padx=20, pady=40)

farbe = tkinter.StringVar()
farbe.set("#FAAC58")

mKontext = tkinter.Menu(fenster)
mKontext["tearoff"] = 0
mKontext.add_radiobutton(label="Braun", variable=farbe,
   value="#FAAC58", command=farbwechsel)
mKontext.add_radiobutton(label="Grün", variable=farbe,
   value="#ACFA58", command=farbwechsel)

buEnde = tkinter.Button(fenster, text="Ende", command=ende, width=10)
buEnde.grid(row=0, column=1, padx=20, pady=20)

fenster.mainloop()

