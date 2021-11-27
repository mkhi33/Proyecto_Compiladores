import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from nucleo.pantallas.GUI_AcercaDe import Ui_MainWindow

class GuiAcercaDe(QMainWindow):
    def __init__(self, parent = None):
        super(GuiAcercaDe, self).__init__(parent)
        self.uiAcercaDe = Ui_MainWindow()
        self.uiAcercaDe.setupUi(self)