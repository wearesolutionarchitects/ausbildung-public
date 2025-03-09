import tkinter, os, sqlite3, random,  tkinter.messagebox as mb

# Datenbank und Liste erzeugen, falls Datenbank nicht vorhanden
def erzeugen():
    li = [[1, "Bedingung", "condition"],
          [2, "suchen", "to look for"],
          [3, "Werbeanzeige", "advertisement"],
          [4, "abkürzen", "to abbreviate"],
          [5, "nützlich", "useful"],
          [6, "Wirkung", "effect"],
          [7, "beraten", "to advise"],
          [8, "übersetzen", "to translate"],
          [9, "einfach", "easy"],
          [10, "ankündigen", "to announce"]]
    connection = sqlite3.connect("lernen.db")
    cursor = connection.cursor()
    sql = "CREATE TABLE vokabel(id INTEGER PRIMARY KEY, deutsch TEXT, englisch TEXT)"
    cursor.execute(sql)
    for z in li:
        sql = "INSERT INTO vokabel VALUES(" + str(z[0]) + ", '" + z[1] + "', '" + z[2] + "')"
        cursor.execute(sql)
        connection.commit()
    connection.close()
    return li

# Liste erzeugen, falls Datenbank vorhanden
def laden():
    li = []
    connection = sqlite3.connect("lernen.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM vokabel"
    cursor.execute(sql)
    for dsatz in cursor:
        li.append([dsatz[0], dsatz[1], dsatz[2]])
    connection.close()
    return li

# Liste anzeigen
def alle(li):
    liAuswahl.delete(0, "end")
    for z in li:
        liAuswahl.insert("end", str(z[0]) + " / " + z[1] + " / " + z[2])

# Einzelne Elemente anzeigen
def lernen(li):
    liAuswahl.delete(0, "end")
    z = random.choice(li)
    mb.showinfo("Lernen", z[1] + " / " + z[2])

# Erste / nächste Vokabel erfragen
def frage(li):
    liAuswahl.delete(0, "end")

    global x
    if li:
        x = random.randint(0, len(li) - 1)
        mb.showinfo("Test, noch " + str(len(li)), li[x][1])
        buFrage["state"] = "disabled"
        buPruefen["state"] = "normal"
    else:
        mb.showinfo("Ende", "Gratuliere! Alles geschafft")

# Antwort prüfen
def pruefen(li):
    liAuswahl.delete(0, "end")

    global x
    if etEnglisch.get() == li[x][2]:
        mb.showinfo("Antwort", "Richtig, Vokabel wird aus dem Test genommen")
        del li[x]
    else:
        mb.showinfo("Antwort", "Leider falsch, richtig wäre: " + li[x][2])
    buPruefen["state"] = "disabled"
    buFrage["state"] = "normal"
    etEnglisch.delete(0, "end")

# Programm beenden
def ende(li):
    if li:
        if mb.askokcancel("Noch nicht alles getestet", "Wirklich beenden?") == 0:
            return
    fenster.destroy()

# Hauptprogramm
random.seed()

# Liste erzeugen, ggf. Datenbank erzeugen
if not os.path.exists("lernen.db"):
    li = erzeugen()
else:
    li = laden()

# Fenster
fenster = tkinter.Tk()
fenster.title("Vokabeln")
fenster.resizable(0, 0)

# Widgets in Zeile 0
buAlle = tkinter.Button(fenster, text="Alle anzeigen", command=lambda:alle(li), width=15)
buAlle.grid(row=0, column=0, padx=5, pady=5)

buLernen = tkinter.Button(fenster, text="Einzeln lernen", command=lambda:lernen(li), width=15)
buLernen.grid(row=0, column=1, padx=5, pady=5)

buEnde = tkinter.Button(fenster, text="Ende", command=lambda:ende(li), width=15)
buEnde.grid(row=0, column=2, padx=5, pady=5)

# Widgets in Zeile 1
buFrage = tkinter.Button(fenster, text="Frage", command=lambda:frage(li), width=15)
buFrage.grid(row=1, column=0, padx=5, pady=5)

etEnglisch = tkinter.Entry(fenster)
etEnglisch.grid(row=1, column=1, padx=5, pady=5)

buPruefen = tkinter.Button(fenster, text="Prüfen", command=lambda:pruefen(li), state="disabled", width=15)
buPruefen.grid(row=1, column=2, padx=5, pady=5)

# Frame mit Listbox und Scrollbar in Zeile 2
frAuswahl = tkinter.Frame(fenster)
frAuswahl.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

sbAuswahl = tkinter.Scrollbar(frAuswahl, orient="vertical")
liAuswahl = tkinter.Listbox(frAuswahl, width=50, height=4, yscrollcommand=sbAuswahl.set)
sbAuswahl["command"] = liAuswahl.yview
liAuswahl.grid(row=0, column=0)
sbAuswahl.grid(row=0, column=1, sticky="sn")

# Endlos-Schleife
fenster.mainloop()
