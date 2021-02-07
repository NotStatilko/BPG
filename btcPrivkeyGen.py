# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'btcPrivkeyGen.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(271, 275)
        mainWindow.setMinimumSize(QtCore.QSize(271, 275))
        mainWindow.setMaximumSize(QtCore.QSize(271, 275))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 30, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 150, 171, 25))
        self.pushButton.setStyleSheet("background-color: rgb(24, 24, 24);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(20, 19, 19);")
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 100, 211, 25))
        self.lineEdit.setMinimumSize(QtCore.QSize(211, 0))
        self.lineEdit.setStyleSheet("selection-color: rgb(255, 255, 255);\n"
"gridline-color: rgb(24, 24, 24);\n"
"selection-background-color: rgb(24, 24, 24);")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 200, 211, 25))
        self.lineEdit_2.setMinimumSize(QtCore.QSize(211, 0))
        self.lineEdit_2.setStyleSheet("selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(24, 24, 24);\n"
"gridline-color: rgb(24, 24, 24);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "btcPrivkeyGen"))
        self.label.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ce5c00;\">BTC</span><span style=\" font-size:20pt;\">PrivkeyGen</span></p></body></html>"))
        self.pushButton.setText(_translate("mainWindow", "Generate Key"))
        self.lineEdit.setPlaceholderText(_translate("mainWindow", "         Enter here your seed"))
        self.lineEdit_2.setPlaceholderText(_translate("mainWindow", "  Your private key will be here"))
