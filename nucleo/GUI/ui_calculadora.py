import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from nucleo.pantallas.GUI_Calculadora import Ui_MainWindow

class GuiCalculadora(QMainWindow):
    def __init__(self, parent = None):
        super(GuiCalculadora, self).__init__(parent)
        self.uiCalculadora = Ui_MainWindow()
        self.uiCalculadora.setupUi(self)