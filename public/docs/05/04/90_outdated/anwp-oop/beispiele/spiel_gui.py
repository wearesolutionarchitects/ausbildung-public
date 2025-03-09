import time, random, glob, sqlite3, tkinter, tkinter.messagebox as mb

def auswertung():
    global ergebnisListe, startzeit

    differenz = time.time() - startzeit
    richtig = 0
    for i in range(5):
        try:
            if int(eingabeListe[i].get()) == ergebnisListe[i]:
                richtig += 1
        except:
            pass

    if richtig < 5:
        mb.showinfo("Kein Highscore", "Leider kein Highscore")
        fenster.destroy()
        return
    
    if not glob.glob("spiel_gui_highscore.db"):
        con = sqlite3.connect("spiel_gui_highscore.db")
        cursor = con.cursor()
        sql = "CREATE TABLE daten(name TEXT, zeit REAL)"
        cursor.execute(sql)
        con.close()

    con = sqlite3.connect("spiel_gui_highscore.db")
    cursor = con.cursor()
    sql = f"INSERT INTO daten VALUES(?,{differenz})"
    cursor.execute(sql, (enName.get(), ))
    con.commit()
    con.close()

    con = sqlite3.connect("spiel_gui_highscore.db")
    cursor = con.cursor()
    sql = "SELECT * FROM daten ORDER BY zeit LIMIT 10"
    cursor.execute(sql)
    ausgabe = ""
    i = 1
    for dsatz in cursor:
        ausgabe += f"{i}. {dsatz[0]} {round(dsatz[1],2)} sec.\n"
        i += 1
    mb.showinfo("Highscore", ausgabe)
    con.close()

    fenster.destroy()

def start():
    global ergebnisListe, startzeit
    ergebnisListe = []
    for i in range(5):
        a = random.randint(10,30)
        b = random.randint(10,30)
        ergebnisListe.append(a + b)
        aufgabeListe[i]["text"] = f"{a} + {b} ="
    startzeit = time.time()
    buAktion["text"] = "Stop"

def aktion():
    if buAktion["text"] == "Start":
        if enName.get() == "":
            mb.showinfo("Name","Bitte einen Namen eintragen")
        else:
            start()
    else:
        auswertung()

# Programm
fenster = tkinter.Tk()
fenster.title("Kopfrechnen")
fenster.resizable(0, 0)

lbName = tkinter.Label(fenster, text="Ihr Name:")
lbName.grid(row=0, column=0, sticky="w", padx=5, pady=10)
enName = tkinter.Entry(fenster, width=15)
enName.grid(row=0, column=2, pady=10)
buAktion = tkinter.Button(fenster, text="Start", width=10, command=aktion)
buAktion.grid(row=1, column=0, columnspan=3, pady=10)

aufgabeListe = []
eingabeListe = []
for i in range(5):
    lbTemp = tkinter.Label(fenster, text=f"Aufgabe {i+1}:")
    lbTemp.grid(row=i+2, column=0, padx=5, pady=5)
    lbTemp = tkinter.Label(fenster, width=10, pady=5)
    lbTemp.grid(row=i+2, column=1, pady=5)
    aufgabeListe.append(lbTemp)
    enTemp = tkinter.Entry(fenster, width=15)
    enTemp.grid(row=i+2, column=2, padx=10, pady=5)
    eingabeListe.append(enTemp)

fenster.mainloop()
