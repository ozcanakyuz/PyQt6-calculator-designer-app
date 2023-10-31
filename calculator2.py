import sys
from PyQt6 import QtWidgets
from calculator import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_topla.clicked.connect(self.hesapla)
        self.ui.btn_cikar.clicked.connect(self.hesapla)
        self.ui.btn_carp.clicked.connect(self.hesapla)
        self.ui.btn_bol.clicked.connect(self.hesapla)

    def hesapla(self):
        sender = self.sender().text()
        result = 0

        if sender == '+':
            result = int(self.ui.txt_sayi1.text()) + int(self.ui.txt_sayi2.text())
        elif sender == '-':
            result = int(self.ui.txt_sayi1.text()) - int(self.ui.txt_sayi2.text())
        elif sender == '*':
            result = int(self.ui.txt_sayi1.text()) * int(self.ui.txt_sayi2.text())
        elif sender == '/':
            result = int(self.ui.txt_sayi1.text()) / int(self.ui.txt_sayi2.text())

        self.ui.lbl_result.setText(str(result))
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())

app()
