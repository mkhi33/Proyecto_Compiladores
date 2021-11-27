import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QDialog
from nucleo.pantallas.GUI_Dialogo import Ui_Dialog

class GUIDialogo(QMainWindow):
    def __init__(self, parent = None):
        super(GUIDialogo, self).__init__(parent)
        self.uiDialogo = Ui_Dialog()
        self.uiDialogo.setupUi(self)