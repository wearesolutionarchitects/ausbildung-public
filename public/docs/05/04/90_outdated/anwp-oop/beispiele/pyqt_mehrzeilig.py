import PyQt6.QtWidgets as wi
import sys

class Fenster(wi.QWidget):
    def __init__(self):
        super().__init__()
        gr = wi.QGridLayout()

        lbText = wi.QLabel("Text:")
        gr.addWidget(lbText, 0, 0)

        self.teText = wi.QTextEdit()
        self.teText.setFixedHeight(80)
        gr.addWidget(self.teText, 1, 0, 1, 3)

        buLaden = wi.QPushButton("Aus Datei laden")
        buLaden.clicked.connect(self.laden)
        gr.addWidget(buLaden, 2, 0)

        buSpeichern = wi.QPushButton("In Datei speichern")
        buSpeichern.clicked.connect(self.speichern)
        gr.addWidget(buSpeichern, 2, 1)

        buLoeschen = wi.QPushButton("Text löschen")
        buLoeschen.clicked.connect(self.loeschen)
        gr.addWidget(buLoeschen, 2, 2)

        self.lbAusgabe = wi.QLabel("(leer)")
        gr.addWidget(self.lbAusgabe, 3, 0)

        self.buEnde = wi.QPushButton("Ende")
        self.buEnde.clicked.connect(wi.QApplication.instance().quit)
        gr.addWidget(self.buEnde, 3, 3)

        self.setWindowTitle("TextEdit")
        self.setLayout(gr)
        self.show()

    def laden(self):
        self.teText.setText("")
        try:
            d = open("pyqt_mehrzeilig.txt")
            self.teText.setText(d.read())
            d.close()
        except:
            self.teText.setText("Datei nicht geöffnet")

    def speichern(self):
        try:
            d = open("pyqt_mehrzeilig.txt", "w")
            d.write(self.teText.toPlainText())
            d.close()
        except:
            self.lbAusgabe.setText("Datei nicht geöffnet")

    def loeschen(self):
        self.teText.setText("")

anwendung = wi.QApplication(sys.argv)
fenster = Fenster()
sys.exit(anwendung.exec())
