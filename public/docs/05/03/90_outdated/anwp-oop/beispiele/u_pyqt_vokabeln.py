import PyQt6.QtWidgets as wi
import sys, os, sqlite3, random

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

# Klasse
class Fenster(wi.QWidget):
    def __init__(self):
        super().__init__()
        gr = wi.QGridLayout()

        # Liste erzeugen, ggf. Datenbank erzeugen
        if not os.path.exists("lernen.db"):
            self.li = erzeugen()
        else:
            self.li = laden()

        # Widgets in Zeile 0
        buAlle = wi.QPushButton("Alle anzeigen")
        buAlle.clicked.connect(self.alle)
        gr.addWidget(buAlle, 0, 0)

        buLernen = wi.QPushButton("Einzeln lernen")
        buLernen.clicked.connect(self.lernen)
        gr.addWidget(buLernen, 0, 1)

        buEnde = wi.QPushButton("Ende")
        buEnde.clicked.connect(self.ende)
        gr.addWidget(buEnde, 0, 2)

        # Widgets in Zeile 1
        self.buFrage = wi.QPushButton("Frage")
        self.buFrage.clicked.connect(self.frage)
        gr.addWidget(self.buFrage, 1, 0)

        self.leEingabe = wi.QLineEdit()
        gr.addWidget(self.leEingabe, 1, 1)

        self.buPruefen = wi.QPushButton("Prüfen")
        self.buPruefen.clicked.connect(self.pruefen)
        self.buPruefen.setEnabled(False)
        gr.addWidget(self.buPruefen, 1, 2)

        # ListBox in Zeile 2
        self.liAuswahl = wi.QListWidget()
        self.liAuswahl.setFixedHeight(80)
        gr.addWidget(self.liAuswahl, 2, 0, 1, 3)

        # GUI anzeigen
        self.setWindowTitle("Vokabeln")
        self.setLayout(gr)
        self.show()

    # Hilfsmethode: Anzeige einer Info-Meldung
    def meldung(self, titel, info):
        mb = wi.QMessageBox(self)
        mb.setWindowTitle(titel)
        mb.setText(info)
        mb.exec()

    # Liste anzeigen
    def alle(self):
        self.liAuswahl.clear()
        for z in self.li:
            self.liAuswahl.addItem(str(z[0]) + " / " + z[1] + " / " + z[2])

    # Einzelne Elemente anzeigen
    def lernen(self):
        self.liAuswahl.clear()
        z = random.choice(self.li)
        self.meldung("Lernen", z[1] + " / " + z[2])

    # Erste / nächste Vokabel erfragen
    def frage(self):
        self.liAuswahl.clear()
        if self.li:
            self.x = random.randint(0, len(self.li) - 1)
            self.meldung(str(len(self.li)), self.li[self.x][1])
            self.buFrage.setEnabled(False)
            self.buPruefen.setEnabled(True)
        else:
            self.meldung("Ende", "Gratuliere! Alles geschafft")

    # Antwort prüfen
    def pruefen(self):
        self.liAuswahl.clear()
        if self.leEingabe.text() == self.li[self.x][2]:
            self.meldung("Antwort", "Richtig, Vokabel wird aus dem Test genommen")
            del self.li[self.x]
        else:
            self.meldung("Antwort", "Leider falsch, richtig wäre: " + self.li[self.x][2])
        self.buPruefen.setEnabled(False)
        self.buFrage.setEnabled(True)
        self.leEingabe.setText("")

    # Programm beenden
    def ende(self):
        if self.li:
            mb = wi.QMessageBox(self)
            mb.setWindowTitle("Noch nicht fertig")
            mb.setIcon(wi.QMessageBox.Icon.Question)
            mb.setText("Wirklich beenden?")
            mb.setStandardButtons(wi.QMessageBox.StandardButton.Ok
                | wi.QMessageBox.StandardButton.Abort)
            mb.setDefaultButton(wi.QMessageBox.StandardButton.Abort)
            if mb.exec() == wi.QMessageBox.StandardButton.Abort:
                return
        wi.QApplication.instance().quit()

# Hauptprogramm
random.seed()
anwendung = wi.QApplication(sys.argv)
fenster = Fenster()
sys.exit(anwendung.exec())
