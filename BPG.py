from btcPrivkeyGen import Ui_mainWindow
from PyQt5 import QtWidgets, QtCore
from sys import exit as sys_exit
from bitcoin import bip32_master_key

class bpg(QtWidgets.QMainWindow):
    def __init__(self):
        super(bpg, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.on_click)

    def on_click(self):
        filled_with = self.ui.lineEdit.text()
        if filled_with:
            self.ui.lineEdit_2.setText(bip32_master_key(filled_with))

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = bpg()
    application.show()

    sys_exit(app.exec())
                          
