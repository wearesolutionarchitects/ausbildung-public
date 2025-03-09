import tkinter

def hallo():
    lbAusgabe["text"] = "Hallo"

def ende():
    fenster.destroy()

fenster = tkinter.Tk()
fenster.title("GUI")
fenster.geometry("245x105+200+50")
fenster.resizable(0, 0)

buHallo = tkinter.Button(fenster, text="Hallo", command=hallo, width=10)
buHallo.place(x=5, y=5)

lbAusgabe = tkinter.Label(fenster, text="(leer)",
    anchor="w", relief="sunken", width=20)
lbAusgabe.place(x=5, y=40)

buEnde = tkinter.Button(fenster, text="Ende", command=ende, width=10)
buEnde.place(x=160, y=75)

fenster.mainloop()
