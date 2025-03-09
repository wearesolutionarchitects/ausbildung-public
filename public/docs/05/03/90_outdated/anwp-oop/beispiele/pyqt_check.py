import PyQt6.QtWidgets as wi
import sys

class Fenster(wi.QWidget):
    def __init__(self):
        super().__init__()
        gr = wi.QGridLayout()

        self.lbAuswahl = wi.QLabel("Ihre Auswahl:")
        gr.addWidget(self.lbAuswahl, 0, 0, 1, 2)

        self.cbRahmen = wi.QCheckBox("Rahmen")
        self.cbRahmen.stateChanged.connect(self.aendern)
        gr.addWidget(self.cbRahmen, 1, 0)

        self.cbFuellung = wi.QCheckBox("Füllung")
        self.cbFuellung.setChecked(True)
        self.cbFuellung.stateChanged.connect(self.aendern)
        gr.addWidget(self.cbFuellung, 1, 1)

        buAusgabe = wi.QPushButton("Ausgabe")
        buAusgabe.clicked.connect(self.ausgabe)
        gr.addWidget(buAusgabe, 2, 0, 1, 2)

        buEnde = wi.QPushButton("Ende")
        buEnde.clicked.connect(wi.QApplication.instance().quit)
        gr.addWidget(buEnde, 3, 2)

        self.setWindowTitle("Checkbox")
        self.setLayout(gr)
        self.show()

    def aendern(self):
        cb = self.sender()
        tx = cb.text()
        if cb.isChecked():
            self.lbAuswahl.setText(f"{tx}: Ja")
        else:
            self.lbAuswahl.setText(f"{tx}: Nein")
    
    def ausgabe(self):
        if self.cbRahmen.isChecked():
            tx = "Rahmen: Ja, "
        else:
            tx = "Rahmen: Nein, "
        if self.cbFuellung.isChecked():
            tx += "Füllung: Ja"
        else:
            tx += "Füllung: Nein"
        self.lbAuswahl.setText(tx)

anwendung = wi.QApplication(sys.argv)
fenster = Fenster()
sys.exit(anwendung.exec())
