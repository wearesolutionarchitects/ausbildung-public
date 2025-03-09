import PyQt6.QtWidgets as wi
import PyQt6.QtCore as co
import sys

class Fenster(wi.QWidget):
    def __init__(self):
        super().__init__()
        gr = wi.QGridLayout()

        self.lbAuswahl = wi.QLabel("Wert: 24")
        gr.addWidget(self.lbAuswahl, 0, 0)

        self.slWert = wi.QSlider()
        self.slWert.setFixedWidth(200)
        self.slWert.setOrientation(co.Qt.Orientation.Horizontal)
        self.slWert.setMinimum(10)
        self.slWert.setMaximum(50)
        self.slWert.setValue(24)
        self.slWert.setSingleStep(2)
        self.slWert.setPageStep(10)
        self.slWert.setTickPosition(wi.QSlider.TickPosition.TicksBelow)
        self.slWert.setTickInterval(5)
        self.slWert.valueChanged.connect(self.aendern)
        gr.addWidget(self.slWert, 1, 0)

        buAusgabe = wi.QPushButton("Ausgabe")
        buAusgabe.clicked.connect(self.ausgabe)
        gr.addWidget(buAusgabe, 2, 0)

        buEnde = wi.QPushButton("Ende")
        buEnde.clicked.connect(wi.QApplication.instance().quit)
        gr.addWidget(buEnde, 3, 1)

        self.setWindowTitle("Slider")
        self.setLayout(gr)
        self.show()

    def aendern(self, wert):
        self.lbAuswahl.setText(f"Nach Änderung: {wert}")
    
    def ausgabe(self):
        wert = self.slWert.value()
        self.lbAuswahl.setText(f"Ausgabe: {wert}")

anwendung = wi.QApplication(sys.argv)
fenster = Fenster()
sys.exit(anwendung.exec())
