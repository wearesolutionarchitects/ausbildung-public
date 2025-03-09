import PyQt6.QtWidgets as wi
import PyQt6.QtGui as gu
import PyQt6.QtCore as co
import sys

class Fenster(wi.QWidget):
    def __init__(self):
        super().__init__()
        gr = wi.QGridLayout()

        lbBild = wi.QLabel()
        pm = gu.QPixmap("rheinwerk.png")
        lbBild.setPixmap(pm)
        gr.addWidget(lbBild, 0, 0)

        lbFarbe = wi.QLabel("Text")
        lbFarbe.setFixedHeight(50)
        lbFarbe.setStyleSheet(
            "background-color:#A0A0A0; border:2px solid #000000;")
        lbFarbe.setAlignment(
            co.Qt.AlignmentFlag.AlignBottom | co.Qt.AlignmentFlag.AlignRight)
        gr.addWidget(lbFarbe, 1, 0)

        lbLink = wi.QLabel(
            "<a href='https://www.rheinwerk-verlag.de/'>Rheinwerk-Verlag</a>")
        lbLink.setOpenExternalLinks(True)
        gr.addWidget(lbLink, 2, 0)

        buEnde = wi.QPushButton("Ende")
        buEnde.clicked.connect(wi.QApplication.instance().quit)
        gr.addWidget(buEnde, 3, 0)

        self.setWindowTitle("Label")
        self.setLayout(gr)
        self.show()

anwendung = wi.QApplication(sys.argv)
fenster = Fenster()
sys.exit(anwendung.exec())
