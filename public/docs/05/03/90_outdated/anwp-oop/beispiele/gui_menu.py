import tkinter

def farbwechsel():
    lbHallo["bg"] = farbe.get()

def randwechsel():
    lbHallo["relief"] = rand.get()

def ende():
    fenster.destroy()

fenster = tkinter.Tk()
fenster.title("Menü")
fenster.resizable(0, 0)

lbHallo = tkinter.Label(fenster, text="Hallo", width=30, bg="#FAAC58")
lbHallo.grid(row=0, column=0, padx=20, pady=40)

mLeiste = tkinter.Menu(fenster)

mDatei = tkinter.Menu(mLeiste)
mDatei.add_command(label="Neu")
mDatei.add_command(label="Öffnen")
mDatei.add_separator()
mDatei.add_command(label="Beenden", command=ende)

mAnsicht = tkinter.Menu(mLeiste)
mAnsicht["tearoff"] = 0

farbe = tkinter.StringVar()
farbe.set("#FAAC58")
mAnsicht.add_radiobutton(label="Braun", variable=farbe,
   value="#FAAC58", underline=0, command=farbwechsel)
mAnsicht.add_radiobutton(label="Grün", variable=farbe,
   value="#ACFA58", underline=0, command=farbwechsel)
mAnsicht.add_separator()

rand = tkinter.StringVar()
rand.set("flat")
mAnsicht.add_checkbutton(label="Rand", variable=rand,
    onvalue="solid", offvalue="flat", underline=0, command=randwechsel)

mLeiste.add_cascade(label="Datei", menu=mDatei)
mLeiste.add_cascade(label="Ansicht", menu=mAnsicht)
fenster["menu"] = mLeiste

fenster.mainloop()

