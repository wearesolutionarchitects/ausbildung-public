import PyQt6.QtWidgets as wi
import sys

class Fenster(wi.QWidget):
    def __init__(self):
        super().__init__()
        gr = wi.QGridLayout()

        self.lbAuswahl = wi.QLabel("Ihre Auswahl:")
        gr.addWidget(self.lbAuswahl, 0, 0, 1, 3)

        rbRot = wi.QRadioButton("Rot")
        gr.addWidget(rbRot, 1, 0)

        rbGelb = wi.QRadioButton("Gelb")
        rbGelb.setChecked(True)
        gr.addWidget(rbGelb, 1, 1)

        rbBlau = wi.QRadioButton("Blau")
        gr.addWidget(rbBlau, 1, 2)

        self.gpFarbe = wi.QButtonGroup()
        self.gpFarbe.addButton(rbRot)
        self.gpFarbe.addButton(rbGelb)
        self.gpFarbe.addButton(rbBlau)
        self.gpFarbe.buttonClicked.connect(self.auswahl)
        
        rbKlein = wi.QRadioButton("klein")
        gr.addWidget(rbKlein, 2, 0)

        rbMittel = wi.QRadioButton("mittel")
        gr.addWidget(rbMittel, 2, 1)

        rbGross = wi.QRadioButton("groß")
        rbGross.setChecked(True)
        gr.addWidget(rbGross, 2, 2)

        self.gpGroesse = wi.QButtonGroup()
        self.gpGroesse.addButton(rbKlein)
        self.gpGroesse.addButton(rbMittel)
        self.gpGroesse.addButton(rbGross)
        self.gpGroesse.buttonClicked.connect(self.auswahl)
        
        buAusgabe = wi.QPushButton("Ausgabe")
        buAusgabe.clicked.connect(self.ausgabe)
        gr.addWidget(buAusgabe, 3, 0, 1, 3)

        buEnde = wi.QPushButton("Ende")
        buEnde.clicked.connect(wi.QApplication.instance().quit)
        gr.addWidget(buEnde, 4, 3)

        self.setWindowTitle("Gruppe")
        self.setLayout(gr)
        self.show()

    def ausgabe(self):
        rbFarbe = self.gpFarbe.checkedButton()
        rbGroesse = self.gpGroesse.checkedButton()
        self.lbAuswahl.setText(
            f"Ausgabe: {rbFarbe.text()} und {rbGroesse.text()}")

    def auswahl(self, rb):
        self.lbAuswahl.setText(f"Auswahl: {rb.text()}")

anwendung = wi.QApplication(sys.argv)
fenster = Fenster()
sys.exit(anwendung.exec())
