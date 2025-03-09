import PyQt6.QtWidgets as wi
import sys

class Fenster(wi.QWidget):
    def __init__(self):
        super().__init__()
        gr = wi.QGridLayout()

        self.lbErgebnis = wi.QLabel("Ihre Auswahl oder Eingabe:")
        self.lbErgebnis.setFixedWidth(150)
        gr.addWidget(self.lbErgebnis, 0, 0)

        self.spAuswahlInt = wi.QSpinBox()
        self.spAuswahlInt.setMinimum(10)
        self.spAuswahlInt.setMaximum(30)
        self.spAuswahlInt.setSingleStep(2)
        self.spAuswahlInt.setValue(16)
        self.spAuswahlInt.valueChanged.connect(self.aendern)
        gr.addWidget(self.spAuswahlInt, 1, 0)
        
        self.spAuswahlDbl = wi.QDoubleSpinBox()
        self.spAuswahlDbl.setMinimum(2.8)
        self.spAuswahlDbl.setMaximum(7.2)
        self.spAuswahlDbl.setSingleStep(0.2)
        self.spAuswahlDbl.setValue(3.4)
        self.spAuswahlDbl.setDecimals(1)
        self.spAuswahlDbl.valueChanged.connect(self.aendern)
        gr.addWidget(self.spAuswahlDbl, 2, 0)
        
        buAusgabe = wi.QPushButton("Ausgabe")
        buAusgabe.clicked.connect(self.ausgabe)
        gr.addWidget(buAusgabe, 3, 0)

        buEnde = wi.QPushButton("Ende")
        buEnde.clicked.connect(wi.QApplication.instance().quit)
        gr.addWidget(buEnde, 4, 1)

        self.setWindowTitle("Spinbox")
        self.setLayout(gr)
        self.show()

    def aendern(self, wert):
        if self.sender() is self.spAuswahlInt:
            self.lbErgebnis.setText(f"Änderung: {wert}")
        else:
            self.lbErgebnis.setText(f"Änderung: {round(wert,1)}")
    
    def ausgabe(self):
        wertInt = self.spAuswahlInt.value()
        wertDbl = round(self.spAuswahlDbl.value(), 1)
        self.lbErgebnis.setText(f"Ausgabe: {wertInt} und {wertDbl}")

anwendung = wi.QApplication(sys.argv)
fenster = Fenster()
sys.exit(anwendung.exec())
