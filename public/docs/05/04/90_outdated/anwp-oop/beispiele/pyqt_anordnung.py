import PyQt6.QtWidgets as wi
import sys

class Fenster(wi.QWidget):
    def __init__(self):
        super().__init__()
        gr = wi.QGridLayout()

        buHallo = wi.QPushButton("Hallo")
        buHallo.clicked.connect(self.hallo)
        gr.addWidget(buHallo, 0, 0)

        self.lbAusgabe = wi.QLabel("(leer)")
        gr.addWidget(self.lbAusgabe, 1, 0)

        buEnde = wi.QPushButton("Ende")
        buEnde.clicked.connect(wi.QApplication.instance().quit)
        gr.addWidget(buEnde, 2, 1)

        self.setWindowTitle("...")
        self.setLayout(gr)
        self.show()

    def hallo(self):
        self.lbAusgabe.setText("Hallo")

anwendung = wi.QApplication(sys.argv)
fenster = Fenster()
sys.exit(anwendung.exec())
