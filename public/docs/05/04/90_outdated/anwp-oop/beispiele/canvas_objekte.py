import tkinter

fenster = tkinter.Tk()
fenster.title("Canvas, Objekte")
fenster.geometry("400x200")
fenster.resizable(0, 0)

cv = tkinter.Canvas(fenster, bg="#E0E0E0")
cv.pack(fill="both", expand=True)
cv.create_line((20, 50), (70, 50), (70, 150),
               fill="#A0A0A0", width=3, arrow="last")
cv.create_rectangle((90, 50), (140, 150),
                    fill="#A0A0A0", outline="#FFFFFF", width=3)
cv.create_oval((160, 50), (210, 150), fill="#A0A0A0", width=0)
cv.create_polygon((230, 50), (280, 50), (280, 150), fill="#A0A0A0")
cv.create_text(300, 50, text="Hallo", anchor="nw")

fenster.mainloop()
