import tkinter

fenster = tkinter.Tk()
fenster.title("GUI")
fenster.geometry("300x225")
fenster.minsize(200, 150)
fenster.maxsize(400, 300)

bu1 = tkinter.Button(fenster, text="1", width=5)
bu1.place(relx=0.05, rely=0.05)

bu2 = tkinter.Button(fenster, text="2", width=5)
bu2.place(relx=0.5, rely=0.05, anchor="n")

bu3 = tkinter.Button(fenster, text="3", width=5)
bu3.place(relx=0.95, rely=0.05, anchor="ne")

bu4 = tkinter.Button(fenster, text="4", width=5)
bu4.place(relx=0.05, rely=0.5, anchor="w")

bu5 = tkinter.Button(fenster, text="5", width=5)
bu5.place(relx=0.5, rely=0.5, anchor="center")

bu6 = tkinter.Button(fenster, text="6", width=5)
bu6.place(relx=0.95, rely=0.5, anchor="e")

bu7 = tkinter.Button(fenster, text="7", width=5)
bu7.place(relx=0.05, rely=0.95, anchor="sw")

bu8 = tkinter.Button(fenster, text="8", width=5)
bu8.place(relx=0.5, rely=0.95, anchor="s")

bu9 = tkinter.Button(fenster, text="9", width=5)
bu9.place(relx=0.95, rely=0.95, anchor="se")

fenster.mainloop()
