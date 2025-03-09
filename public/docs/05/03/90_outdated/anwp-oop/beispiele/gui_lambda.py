import tkinter

def aus(p):
    lbAusgabe["text"] = p

def ende():
    fenster.destroy()

fenster = tkinter.Tk()
fenster.title("GUI")
fenster.resizable(0, 0)

buEins = tkinter.Button(fenster, text="1", width=10, command=lambda:aus(1))
buEins.grid(row=0, column=0, padx=5, pady=5)

buZwei = tkinter.Button(fenster, text="2", width=10, command=lambda:aus(2))
buZwei.grid(row=1, column=0, padx=5, pady=5)

lbAusgabe = tkinter.Label(fenster, width=20)
lbAusgabe.grid(row=2, column=0, padx=5, pady=5)

fenster.mainloop()
