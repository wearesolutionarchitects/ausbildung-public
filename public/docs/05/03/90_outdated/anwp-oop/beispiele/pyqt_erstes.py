import PyQt6.QtWidgets as wi
import sys

class Fenster(wi.QWidget):
    def __init__(self):
        super().__init__()
        
        buEnde = wi.QPushButton("Ende", self)
        buEnde.move(40, 20)
        instanz = wi.QApplication.instance()
        buEnde.clicked.connect(instanz.quit)
        
        self.setWindowTitle("...")
        self.show()

anwendung = wi.QApplication(sys.argv)
fenster = Fenster()
sys.exit(anwendung.exec())
