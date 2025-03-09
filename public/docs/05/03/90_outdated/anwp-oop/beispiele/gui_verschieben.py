import tkinter, time

posx = 205

def links():
    global posx
    if posx > 80:
        posx -= 20
        buVerschieben.place(x=posx, y=5)

def rechts():
    global posx
    if posx < 340:
        posx += 20
        buVerschieben.place(x=posx, y=5)

fenster = tkinter.Tk()
fenster.title("Verschieben")
fenster.geometry("455x35")
fenster.resizable(0, 0)

buLinks = tkinter.Button(fenster, text="<<", command=links, width=5)
buLinks.place(x=5, y=5)

buVerschieben = tkinter.Button(fenster, text="xxx", width=5)
buVerschieben.place(x=205, y=5)

buRechts = tkinter.Button(fenster, text=">>", command=rechts, width=5)
buRechts.place(x=405, y=5)

fenster.mainloop()

