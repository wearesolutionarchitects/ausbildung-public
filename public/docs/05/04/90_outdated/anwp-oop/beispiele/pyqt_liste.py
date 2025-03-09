import PyQt6.QtWidgets as wi
import sys

class Fenster(wi.QWidget):
    def __init__(self):
        super().__init__()
        gr = wi.QGridLayout()

        lbAuswahl = wi.QLabel("Ihre Auswahl:")
        gr.addWidget(lbAuswahl, 0, 0)

        self.liAuswahl = wi.QListWidget()
        self.liAuswahl.setFixedHeight(80)
        stadt = ["Hamburg", "Stuttgart", "Berlin", "Dortmund", "Trier",
            "Duisburg", "Potsdam", "Halle", "Flensburg", "Augsburg"]
        for s in stadt:
            self.liAuswahl.addItem(s)
        self.liAuswahl.setCurrentRow(0)
        self.liAuswahl.itemClicked.connect(self.auswahl)
        gr.addWidget(self.liAuswahl, 1, 0)
        
        buAusgabe = wi.QPushButton("Ausgabe")
        buAusgabe.clicked.connect(self.ausgabe)
        gr.addWidget(buAusgabe, 2, 0)

        self.lbAusgabe = wi.QLabel("(leer)")
        gr.addWidget(self.lbAusgabe, 3, 0)

        buEnde = wi.QPushButton("Ende")
        buEnde.clicked.connect(wi.QApplication.instance().quit)
        gr.addWidget(buEnde, 4, 1)

        self.setWindowTitle("ListWidget")
        self.setLayout(gr)
        self.show()

    def auswahl(self, it):
        self.lbAusgabe.setText(f"Auswahl: {it.text()}")
    
    def ausgabe(self):
        it = self.liAuswahl.currentItem()
        self.lbAusgabe.setText(f"Ausgabe: {it.text()}")
    
anwendung = wi.QApplication(sys.argv)
fenster = Fenster()
sys.exit(anwendung.exec())
