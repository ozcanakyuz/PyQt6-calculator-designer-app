# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(304, 307)
        MainWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(40, 35, 51, 21))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 75, 51, 21))
        self.label_2.setObjectName("label_2")
        self.txt_sayi1 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_sayi1.setGeometry(QtCore.QRect(90, 30, 131, 31))
        self.txt_sayi1.setObjectName("txt_sayi1")
        self.txt_sayi2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_sayi2.setGeometry(QtCore.QRect(90, 70, 131, 31))
        self.txt_sayi2.setObjectName("txt_sayi2")
        self.btn_topla = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_topla.setGeometry(QtCore.QRect(110, 110, 41, 41))
        self.btn_topla.setObjectName("btn_topla")
        self.btn_cikar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_cikar.setGeometry(QtCore.QRect(160, 110, 41, 41))
        self.btn_cikar.setObjectName("btn_cikar")
        self.btn_carp = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_carp.setGeometry(QtCore.QRect(110, 160, 41, 41))
        self.btn_carp.setObjectName("btn_carp")
        self.btn_bol = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_bol.setGeometry(QtCore.QRect(160, 160, 41, 41))
        self.btn_bol.setObjectName("btn_bol")
        self.lbl_result = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_result.setGeometry(QtCore.QRect(50, 210, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        self.lbl_result.setFont(font)
        self.lbl_result.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.lbl_result.setText("")
        self.lbl_result.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_result.setObjectName("lbl_result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 304, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "SAYI1:"))
        self.label_2.setText(_translate("MainWindow", "SAYI2:"))
        self.btn_topla.setText(_translate("MainWindow", "+"))
        self.btn_cikar.setText(_translate("MainWindow", "-"))
        self.btn_carp.setText(_translate("MainWindow", "*"))
        self.btn_bol.setText(_translate("MainWindow", "/"))
