import PyQt6.QtWidgets as wi
import sys

class Fenster(wi.QWidget):
    def __init__(self):
        super().__init__()
        gr = wi.QGridLayout()

        buInfo = wi.QPushButton("Info")
        buInfo.clicked.connect(self.info)
        gr.addWidget(buInfo, 0, 0)

        buWarning = wi.QPushButton("Warnung")
        buWarning.clicked.connect(self.warning)
        gr.addWidget(buWarning, 0, 1)

        buError = wi.QPushButton("Fehler")
        buError.clicked.connect(self.error)
        gr.addWidget(buError, 0, 2)

        buYesNo = wi.QPushButton("Ja/Nein")
        buYesNo.clicked.connect(self.yesno)
        gr.addWidget(buYesNo, 1, 0)

        buOkAbortRetryIgnore = wi.QPushButton(
            "Ok, Abbrechen, Wiederholen oder Ignorieren")
        buOkAbortRetryIgnore.clicked.connect(self.okabortretryignore)
        gr.addWidget(buOkAbortRetryIgnore, 1, 1, 1, 2)

        self.lbAusgabe = wi.QLabel("(leer)")
        gr.addWidget(self.lbAusgabe, 2, 0)

        buEnde = wi.QPushButton("Ende")
        buEnde.clicked.connect(wi.QApplication.instance().quit)
        gr.addWidget(buEnde, 2, 2)

        self.setWindowTitle("Nachrichten")
        self.setLayout(gr)
        self.show()

    def info(self):
        mb = wi.QMessageBox(self)
        mb.setWindowTitle("Box")
        mb.setIcon(wi.QMessageBox.Icon.Information)
        mb.setText("Info")
        mb.exec()

    def warning(self):
        mb = wi.QMessageBox(self)
        mb.setWindowTitle("Box")
        mb.setIcon(wi.QMessageBox.Icon.Warning)
        mb.setText("Warnung")
        mb.exec()

    def error(self):
        mb = wi.QMessageBox(self)
        mb.setWindowTitle("Box")
        mb.setIcon(wi.QMessageBox.Icon.Critical)
        mb.setText("Fehler")
        mb.exec()

    def yesno(self):
        mb = wi.QMessageBox(self)
        mb.setWindowTitle("Box")
        mb.setIcon(wi.QMessageBox.Icon.Question)
        mb.setText("Ja oder Nein")
        mb.setStandardButtons(wi.QMessageBox.StandardButton.Yes
            | wi.QMessageBox.StandardButton.No)
        mb.setDefaultButton(wi.QMessageBox.StandardButton.No)
        if mb.exec() == wi.QMessageBox.StandardButton.Yes:
            self.lbAusgabe.setText("Ja")
        else:
            self.lbAusgabe.setText("Nein")

    def okabortretryignore(self):
        mb = wi.QMessageBox(self)
        mb.setWindowTitle("Box")
        mb.setIcon(wi.QMessageBox.Icon.Question)
        mb.setText("Abbrechen, Wiederholen oder Ignorieren")
        mb.setStandardButtons(wi.QMessageBox.StandardButton.Ok
            | wi.QMessageBox.StandardButton.Abort
            | wi.QMessageBox.StandardButton.Retry
            | wi.QMessageBox.StandardButton.Ignore)
        mb.setDefaultButton(wi.QMessageBox.StandardButton.Ignore)
        ergebnis = mb.exec()
        if ergebnis == wi.QMessageBox.StandardButton.Ok:
            self.lbAusgabe.setText("Ok")
        elif ergebnis == wi.QMessageBox.StandardButton.Abort:
            self.lbAusgabe.setText("Abbrechen")
        elif ergebnis == wi.QMessageBox.StandardButton.Retry:
            self.lbAusgabe.setText("Wiederholen")
        else:
            self.lbAusgabe.setText("Ignorieren")

anwendung = wi.QApplication(sys.argv)
fenster = Fenster()
sys.exit(anwendung.exec())
