import tkinter

def ende():
    fenster.destroy()

fenster = tkinter.Tk()
fenster.resizable(0, 0)

buEnde = tkinter.Button(fenster, text="Ende", command=ende, width=10)
buEnde.pack(padx=30, pady=30)

fenster.mainloop()
