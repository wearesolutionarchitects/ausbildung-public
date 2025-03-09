import PyQt6.QtWidgets as wi
import os, sys, sqlite3

class Fenster(wi.QWidget):
    def __init__(self):
        super().__init__()
        gr = wi.QGridLayout()

        # Buttons in Spalte 0
        buAlleSehen = wi.QPushButton("Alle sehen")
        buAlleSehen.clicked.connect(self.alleSehen)
        gr.addWidget(buAlleSehen, 0, 0)

        buEinfuegen = wi.QPushButton("Einfügen")
        buEinfuegen.clicked.connect(self.einfuegen)
        gr.addWidget(buEinfuegen, 1, 0)

        buAendern = wi.QPushButton("Ändern")
        buAendern.clicked.connect(self.aendern)
        gr.addWidget(buAendern, 2, 0)

        buLoeschen = wi.QPushButton("Löschen")
        buLoeschen.clicked.connect(self.loeschen)
        gr.addWidget(buLoeschen, 3, 0)

        # Label in Spalte 1
        lbName = wi.QLabel("Name:")
        gr.addWidget(lbName, 1, 1)

        lbVorname = wi.QLabel("Vorname:")
        gr.addWidget(lbVorname, 2, 1)

        lbPersonalnummer = wi.QLabel("Personalnummer:")
        gr.addWidget(lbPersonalnummer, 3, 1)

        lbGehalt = wi.QLabel("Gehalt:")
        gr.addWidget(lbGehalt, 4, 1)

        lbGeburtstag = wi.QLabel("Geburtstag:")
        gr.addWidget(lbGeburtstag, 5, 1)

        # Buttons und Eingabefelder in Spalte 2
        buSuchen = wi.QPushButton("In Name suchen")
        buSuchen.clicked.connect(self.suchen)
        gr.addWidget(buSuchen, 0, 2)

        buEnde = wi.QPushButton("Ende")
        buEnde.clicked.connect(wi.QApplication.instance().quit)
        gr.addWidget(buEnde, 7, 2)

        self.leName = wi.QLineEdit()
        gr.addWidget(self.leName, 1, 2)

        self.leVorname = wi.QLineEdit()
        gr.addWidget(self.leVorname, 2, 2)

        self.lePersonalnummer = wi.QLineEdit()
        gr.addWidget(self.lePersonalnummer, 3, 2)

        self.leGehalt = wi.QLineEdit()
        gr.addWidget(self.leGehalt, 4, 2)

        self.leGeburtstag = wi.QLineEdit()
        gr.addWidget(self.leGeburtstag, 5, 2)

        # List-Widget
        self.liAnzeige = wi.QListWidget()
        self.liAnzeige.setFixedHeight(80)
        self.liAnzeige.itemClicked.connect(self.auswahl)
        gr.addWidget(self.liAnzeige, 6, 0, 1, 3)

        # Python-Liste parallel zur Anzeige im List-Widget
        self.pnummer = []

        # Datenbankdatei prüfen, ggf. erzeugen
        if os.path.exists("firma.db"):
            try:
                connection = sqlite3.connect("firma.db")
                cursor = connection.cursor()
                sql = "SELECT * FROM personen"
                cursor.execute(sql)
            except sqlite3.Error as e:
                self.fehler(e)
        else:
            try:
                connection = sqlite3.connect("firma.db")
                cursor = connection.cursor()
                sql = "CREATE TABLE personen(name TEXT, vorname TEXT," \
                    " personalnummer INTEGER PRIMARY KEY, gehalt REAL," \
                    " geburtstag TEXT)"
                cursor.execute(sql)
            except sqlite3.Error as e:
                self.fehler(e)
        connection.close()

        # Fenster gestalten und anzeigen
        self.setWindowTitle("Datenbank, Verwaltung")
        self.setLayout(gr)
        self.show()

    # Hilfsmethode: Anzeige eines SQLite-Fehlers
    def fehler(self, e):
        mb = wi.QMessageBox(self)
        mb.setWindowTitle("Fehler")
        mb.setText(str(e))
        mb.exec()

    # Hilfsmethode: Anzeige einer Info-Meldung
    def meldung(self, info):
        mb = wi.QMessageBox(self)
        mb.setWindowTitle("Info")
        mb.setText(info)
        mb.exec()

    # Hilfsmethode: Eingabefelder leeren
    def eingabefelder_leeren(self):
        self.leName.setText("")
        self.leVorname.setText("")
        self.lePersonalnummer.setText("")
        self.leGehalt.setText("")
        self.leGeburtstag.setText("")

    # Button "Alle sehen"
    def alleSehen(self):
        self.eingabefelder_leeren()
        self.liAnzeige.clear()
        self.pnummer.clear()

        try:
            connection = sqlite3.connect("firma.db")
            cursor = connection.cursor()
            sql = "SELECT * FROM personen"
            cursor.execute(sql)
            for dsatz in cursor:
                self.liAnzeige.addItem(f"{dsatz[0]} # {dsatz[1]}" \
                    f" # {dsatz[2]} # {dsatz[3]} # {dsatz[4]}")
                self.pnummer.append(dsatz[2])
            if len(self.pnummer) == 0:
                self.meldung("Kein Datensatz")
            self.liAnzeige.setCurrentRow(0)
        except sqlite3.Error as e:
            self.fehler(e)
        connection.close()

    # Auswahl in List-Widget
    def auswahl(self):
        i = self.liAnzeige.currentRow()
        if i == -1:
            self.meldung("Kein Datensatz ausgewählt")
            return
        try:
            connection = sqlite3.connect("firma.db")
            cursor = connection.cursor()
            sql = "SELECT * FROM personen WHERE personalnummer = " \
                + str(self.pnummer[i])
            cursor.execute(sql)
            for dsatz in cursor:
                self.leName.setText(dsatz[0])
                self.leVorname.setText(dsatz[1])
                self.lePersonalnummer.setText(str(dsatz[2]))
                self.leGehalt.setText(str(dsatz[3]))
                self.leGeburtstag.setText(dsatz[4])
        except sqlite3.Error as e:
            self.fehler(e)
        connection.close()

    # Button "Einfügen"
    def einfuegen(self):
        if self.leName.text() == "" or self.lePersonalnummer.text() == "" \
                or self.leGehalt.text() == "":
            self.meldung("Name, Personalnummer oder Gehalt fehlen")
            return
        try:
            connection = sqlite3.connect("firma.db")
            cursor = connection.cursor()
            sql = "INSERT INTO personen VALUES(?, ?, ?, ?, ?)"
            cursor.execute(sql, (self.leName.text(), self.leVorname.text(),
                int(self.lePersonalnummer.text()), float(self.leGehalt.text()),
                self.leGeburtstag.text()))
            connection.commit()
        except sqlite3.Error as e:
            self.fehler(e)
        except Exception as e:
            self.fehler(e)
        connection.close()
        self.alleSehen()

    # Button "Ändern"
    def aendern(self):
        i = self.liAnzeige.currentRow()
        if i == -1:
            self.meldung("Kein Datensatz ausgewählt")
            return
        try:
            connection = sqlite3.connect("firma.db")
            cursor = connection.cursor()
            sql = "UPDATE personen SET name = ?, vorname = ?," \
                " personalnummer = ?, gehalt = ?, geburtstag = ?" \
                " WHERE personalnummer = " + str(self.pnummer[i])
            cursor.execute(sql, (self.leName.text(), self.leVorname.text(),
                int(self.lePersonalnummer.text()), float(self.leGehalt.text()),
                self.leGeburtstag.text()))
            connection.commit()
        except sqlite3.Error as e:
            self.fehler(e)
        except Exception as e:
            self.fehler(e)
        connection.close()
        self.alleSehen()

    # Button "Löschen"
    def loeschen(self):
        i = self.liAnzeige.currentRow()
        if i == -1:
            self.meldung("Kein Datensatz ausgewählt")
            return

        # Rückfrage
        mb = wi.QMessageBox(self)
        mb.setWindowTitle("Frage")
        mb.setText("Wirklich löschen?")
        mb.setStandardButtons(wi.QMessageBox.StandardButton.Yes
            | wi.QMessageBox.StandardButton.No)
        mb.setDefaultButton(wi.QMessageBox.StandardButton.No)
        if mb.exec() == wi.QMessageBox.StandardButton.No:
            return

        # Löschen
        try:
            connection = sqlite3.connect("firma.db")
            cursor = connection.cursor()
            sql = "DELETE FROM personen WHERE personalnummer = " \
                + str(self.pnummer[i])
            cursor.execute(sql)
            connection.commit()
        except sqlite3.Error as e:
            self.fehler(e)
        connection.close()
        self.alleSehen()

    # Button "In Name suchen"
    def suchen(self):
        eingabe = self.leName.text()
        self.eingabefelder_leeren()
        self.liAnzeige.clear()
        self.pnummer.clear()

        try:
            connection = sqlite3.connect("firma.db")
            cursor = connection.cursor()
            sql = "SELECT * FROM personen WHERE name LIKE ?"
            eingabe = '%' + eingabe + '%'
            cursor.execute(sql, (eingabe,))
            for dsatz in cursor:
                self.liAnzeige.addItem(f"{dsatz[0]} # {dsatz[1]}" \
                    f" # {dsatz[2]} # {dsatz[3]} # {dsatz[4]}")
                self.pnummer.append(dsatz[2])
            self.liAnzeige.setCurrentRow(0)
            if len(self.pnummer) == 0:
                self.meldung("Kein passender Datensatz")
        except sqlite3.Error as e:
            self.fehler(e)
        connection.close()

# Anwendung starten und beenden
anwendung = wi.QApplication(sys.argv)
fenster = Fenster()
sys.exit(anwendung.exec())
