import PyQt6.QtWidgets as wi
import sys

class Fenster(wi.QWidget):
    def __init__(self):
        super().__init__()
        gr = wi.QGridLayout()

        lbEingabe = wi.QLabel("Ihre Eingabe:")
        gr.addWidget(lbEingabe, 0, 0)

        self.leEingabe = wi.QLineEdit()
        self.leEingabe.textChanged.connect(self.eingabe)
        gr.addWidget(self.leEingabe, 1, 0)

        buVerdoppeln = wi.QPushButton("Verdoppeln")
        buVerdoppeln.clicked.connect(self.verdoppeln)
        gr.addWidget(buVerdoppeln, 2, 0)

        self.lbAusgabe = wi.QLabel("(leer)")
        gr.addWidget(self.lbAusgabe, 3, 0)

        buEnde = wi.QPushButton("Ende")
        buEnde.clicked.connect(wi.QApplication.instance().quit)
        gr.addWidget(buEnde, 4, 1)

        self.setWindowTitle("Eingabe")
        self.setLayout(gr)
        self.show()

    def eingabe(self, tx):
        self.lbAusgabe.setText(f"Eingabe: {tx}")
    
    def verdoppeln(self):
        try:
            zahl = float(self.leEingabe.text())
            self.lbAusgabe.setText(f"{zahl * 2}")
        except:
            self.lbAusgabe.setText("Keine Zahl")
    
anwendung = wi.QApplication(sys.argv)
fenster = Fenster()
sys.exit(anwendung.exec())
