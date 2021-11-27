import sys
from nucleo.GUI.ui_menu import GUIMenu
from nucleo.pantallas import recursos_rc
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = GUIMenu()
    main.show()
    sys.exit(app.exec_())