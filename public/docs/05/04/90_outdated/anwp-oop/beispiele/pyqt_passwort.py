import PyQt6.QtWidgets as wi
import sys

class Fenster(wi.QWidget):
    def __init__(self):
        super().__init__()
        gr = wi.QGridLayout()

        lbPasswort = wi.QLabel("Ihr Passwort:")
        gr.addWidget(lbPasswort, 0, 0)

        self.lePasswort = wi.QLineEdit()
        self.lePasswort.setEchoMode(wi.QLineEdit.EchoMode.Password)
        gr.addWidget(self.lePasswort, 1, 0)

        buPruefen = wi.QPushButton("Prüfen")
        buPruefen.clicked.connect(self.pruefen)
        gr.addWidget(buPruefen, 2, 0)

        self.lbAusgabe = wi.QLabel("(leer)")
        gr.addWidget(self.lbAusgabe, 3, 0)

        self.buEnde = wi.QPushButton("Ende")
        self.buEnde.setEnabled(False)
        self.buEnde.clicked.connect(wi.QApplication.instance().quit)
        gr.addWidget(self.buEnde, 4, 1)

        self.setWindowTitle("Passwort")
        self.setLayout(gr)
        self.show()

    def pruefen(self):
        pw = self.lePasswort.text()
        if pw == "Bingo":
            self.lbAusgabe.setText("Zugang erlaubt")
        else:
            self.lbAusgabe.setText("Zugang nicht erlaubt")
        self.lePasswort.setText("")
        self.buEnde.setEnabled(True)

anwendung = wi.QApplication(sys.argv)
fenster = Fenster()
sys.exit(anwendung.exec())
