import PyQt6.QtWidgets as wi
import sys

class Fenster(wi.QWidget):
    def __init__(self):
        super().__init__()
        gr = wi.QGridLayout()

        self.lbErgebnis = wi.QLabel("Ihre Auswahl oder Eingabe:")
        gr.addWidget(self.lbErgebnis, 0, 0)

        self.cbAuswahl = wi.QComboBox()
        self.cbAuswahl.setEditable(True)
        stadt = ["Hamburg", "Stuttgart", "Berlin", "Dortmund", "Trier",
            "Duisburg", "Potsdam", "Halle", "Flensburg", "Augsburg"]
        for s in stadt:
            self.cbAuswahl.addItem(s)
        self.cbAuswahl.currentTextChanged.connect(self.eingabe)
        self.cbAuswahl.currentIndexChanged.connect(self.auswahl)
        gr.addWidget(self.cbAuswahl, 1, 0)
        
        buAusgabe = wi.QPushButton("Ausgabe")
        buAusgabe.clicked.connect(self.ausgabe)
        gr.addWidget(buAusgabe, 2, 0)

        buEnde = wi.QPushButton("Ende")
        buEnde.clicked.connect(wi.QApplication.instance().quit)
        gr.addWidget(buEnde, 3, 1)

        self.setWindowTitle("Combobox")
        self.setLayout(gr)
        self.show()

    def auswahl(self, ix):
        tx = self.cbAuswahl.currentText()
        self.lbErgebnis.setText(f"Auswahl: {tx}, Index: {ix}")
    
    def eingabe(self, tx):
        self.lbErgebnis.setText(f"Eingabe: {tx}")
    
    def ausgabe(self):
        tx = self.cbAuswahl.currentText()
        ix = self.cbAuswahl.currentIndex()
        self.lbErgebnis.setText(f"Ausgabe: {tx}, Index: {ix}")

anwendung = wi.QApplication(sys.argv)
fenster = Fenster()
sys.exit(anwendung.exec())
