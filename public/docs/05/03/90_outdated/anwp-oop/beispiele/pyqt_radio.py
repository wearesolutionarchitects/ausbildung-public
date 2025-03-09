import PyQt6.QtWidgets as wi
import sys

class Fenster(wi.QWidget):
    def __init__(self):
        super().__init__()
        gr = wi.QGridLayout()

        self.lbAuswahl = wi.QLabel("Ihre Auswahl:")
        gr.addWidget(self.lbAuswahl, 0, 0, 1, 3)

        self.rbRot = wi.QRadioButton("Rot")
        self.rbRot.toggled.connect(self.auswahl)
        gr.addWidget(self.rbRot, 1, 0)

        self.rbGelb = wi.QRadioButton("Gelb")
        self.rbGelb.setChecked(True)
        self.rbGelb.toggled.connect(self.auswahl)
        gr.addWidget(self.rbGelb, 1, 1)

        self.rbBlau = wi.QRadioButton("Blau")
        self.rbBlau.toggled.connect(self.auswahl)
        gr.addWidget(self.rbBlau, 1, 2)
        
        buAusgabe = wi.QPushButton("Ausgabe")
        buAusgabe.clicked.connect(self.ausgabe)
        gr.addWidget(buAusgabe, 2, 0, 1, 3)

        buEnde = wi.QPushButton("Ende")
        buEnde.clicked.connect(wi.QApplication.instance().quit)
        gr.addWidget(buEnde, 3, 3)

        self.setWindowTitle("Radiobutton")
        self.setLayout(gr)
        self.show()

    def auswahl(self):
        rb = self.sender()
        if rb.isChecked():
            self.lbAuswahl.setText(f"Auswahl: {rb.text()}")
    
    def ausgabe(self):
        if self.rbRot.isChecked():
            rb = self.rbRot
        elif self.rbGelb.isChecked():
            rb = self.rbGelb
        else:
            rb = self.rbBlau
        self.lbAuswahl.setText(f"Ausgabe: {rb.text()}")

anwendung = wi.QApplication(sys.argv)
fenster = Fenster()
sys.exit(anwendung.exec())
