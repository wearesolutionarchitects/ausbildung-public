import tkinter

def animieren():
    x0, y0, x1, y1 = cv.coords(rechteck)
    tx = f"{int(x0)}"
    cv.itemconfigure(ausgabe, text=tx)
    if x0 < 330:
        cv.move(rechteck, 2, 0)
        fenster.after(10, animieren)

fenster = tkinter.Tk()
fenster.title("Canvas, Animation")
fenster.geometry("400x150")
fenster.resizable(0, 0)

cv = tkinter.Canvas(fenster, bg="#E0E0E0")
cv.pack(fill="both", expand=True)

rechteck = cv.create_rectangle((20, 50), (70, 100),
    fill="#A0A0A0", outline="#A0A0A0")
ausgabe = cv.create_text((20, 20), text="", anchor="nw")

fenster.after(100, animieren)
fenster.mainloop()
