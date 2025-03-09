import tkinter

def position():
    x0, y0, x1, y1 = cv.coords(rechteck)
    tx = f"{int(x0)} {int(y0)} {int(x1)} {int(y1)}"
    cv.itemconfigure(ausgabe, text=tx)

def taste(e):
    if e.char == "w":
        cv.move(rechteck, 0, -10)
    elif e.char == "a":
        cv.move(rechteck, -10, 0)
    elif e.char == "s":
        cv.move(rechteck, 0, 10)
    elif e.char == "d":
        cv.move(rechteck, 10, 0)
    position()

fenster = tkinter.Tk()
fenster.title("Canvas, Tasten")
fenster.geometry("400x200")
fenster.resizable(0, 0)

cv = tkinter.Canvas(fenster, bg="#E0E0E0")
cv.bind_all("<Key>", taste)
cv.pack(fill="both", expand=True)
rechteck = cv.create_rectangle((180, 80), (230, 130),
    fill="#A0A0A0", outline="#A0A0A0")
ausgabe = cv.create_text((20, 20), text="", anchor="nw")
position()

fenster.mainloop()
