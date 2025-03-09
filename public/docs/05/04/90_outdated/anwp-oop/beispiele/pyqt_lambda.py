import PyQt6.QtWidgets as wi
import sys

class Fenster(wi.QWidget):
    def __init__(self):
        super().__init__()
        gr = wi.QGridLayout()

        buEins = wi.QPushButton("1")
        buEins.clicked.connect(lambda:self.aus(1))
        gr.addWidget(buEins, 0, 0)

        buZwei = wi.QPushButton("2")
        buZwei.clicked.connect(lambda:self.aus(2))
        gr.addWidget(buZwei, 1, 0)

        self.lbAusgabe = wi.QLabel()
        gr.addWidget(self.lbAusgabe, 2, 0)

        self.setWindowTitle("...")
        self.setLayout(gr)
        self.show()

    def aus(self, p):
        self.lbAusgabe.setText(str(p))

anwendung = wi.QApplication(sys.argv)
fenster = Fenster()
sys.exit(anwendung.exec())
