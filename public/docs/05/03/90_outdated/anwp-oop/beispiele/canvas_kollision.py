import tkinter

def animieren():
    x0, y0, x1, y1 = cv.coords(rechteck)
    treffer = cv.find_overlapping(x0, y0, x1, y1)
    if len(treffer) < 2:
        cv.move(rechteck, 2, 0)
        fenster.after(10, animieren)

fenster = tkinter.Tk()
fenster.title("Canvas, Kollision")
fenster.geometry("400x150")
fenster.resizable(0, 0)

cv = tkinter.Canvas(fenster, bg="#E0E0E0")
cv.pack(fill="both", expand=True)

rechteck = cv.create_rectangle((20, 50), (70, 100),
    fill="#A0A0A0", outline="#A0A0A0")
cv.create_rectangle((220, 50), (270, 100),
    fill="#606060", outline="#606060")

fenster.after(100, animieren)
fenster.mainloop()
