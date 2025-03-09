import tkinter

def erzeugeZwei():
    buZwei["state"] = "disabled"
    buEnde["state"] = "disabled"
    global fensterZwei
    fensterZwei = tkinter.Toplevel(fenster)
    fensterZwei.title("Zwei")
    lbHallo = tkinter.Label(fensterZwei, text="Hallo", width=10)
    lbHallo.grid(row=0, column=0, padx=20, pady=10)
    buEndeZwei = tkinter.Button(fensterZwei, text="Ende Zwei",
        width=10, command=endeZwei)
    buEndeZwei.grid(row=0, column=1, padx=20, pady=10)

def endeZwei():
    buZwei["state"] = "normal"
    buEnde["state"] = "normal"
    fensterZwei.destroy()

def ende():
    fenster.destroy()

fenster = tkinter.Tk()
fenster.title("Fenster")
fenster.resizable(0, 0)
status = "fenster"

buZwei = tkinter.Button(fenster, text="Zwei", width=10, command=erzeugeZwei)
buZwei.grid(row=0, column=0, padx=20, pady=10)

buEnde = tkinter.Button(fenster, text="Ende", width=10, command=ende)
buEnde.grid(row=0, column=1, padx=20, pady=10)

fenster.mainloop()
