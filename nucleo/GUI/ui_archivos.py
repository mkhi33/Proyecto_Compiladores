import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QDesktopWidget
from PyQt5.QtGui import QIcon
 
class UiDialogFile(QWidget):
    """
    Nombre: UiDialogFile
    Hereda: Hereda de Qwidget
    Atributos: Sin atributos.
    """
 
    def __init__(self):

        super().__init__()

 
    def openFileNameDialog(self):  
        """
        Nombre: openFileNameDialog
        Parametros: No recibe parametros.
        Descripción: muestra un DialogFile para abrir un archivo.
        Retorno: Retorna la dirección del archivo.
        """  
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Abrir archivo", "","All Files (*);;Python Files (*.enc)", options=options)
        if fileName:
            return fileName

    def openFolderDialog(self):
        """
        Nombre: openFolderDialog
        Parametros: No recibe parametros.
        Descripción: muestra un DialogFile para abrir una carpeta.
        Retorno: Retorna la dirección de todos los archivos y subdirectorios que contiene esa carpeta..
        """ 
        options = QFileDialog.ShowDirsOnly
        options |= QFileDialog.DontUseNativeDialog
        fileName = QFileDialog.getExistingDirectory(self,"Abrir carpeta", options= options)
        if fileName:
            return fileName
    



        
 
    def openFileNamesDialog(self):   
        """
        Nombre: openFileNamesDialog
        Parametros: No recibe parametros.
        Descripción: muestra un DialogFile para abrir una Archivo o varios archivos.
        Retorno: Retorna la dirección de todos los archivos.
        """ 
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"Abrir Archivo", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            
            return ",".join(files)
        else:
            return False

 
    def saveFileDialog(self): 
        """
        Nombre: saveFileDialog
        Parametros: No recibe parametros.
        Descripción: muestra un DialogFile para guardar un archivo.
        Retorno: Retorna la dirección del archivo a guardar.
        """ 
        fileDialog = QFileDialog(self) 
        options = fileDialog.Options()
        options |= fileDialog.DontUseNativeDialog
        rute = fileDialog.getExistingDirectory(caption= "Ruta destino",directory="", options=options)
        if rute:
            return "".join(rute)
        else:
            return False

    """
    Nombre: centerWindow
    Parametros: No recibe parametros
    Descripcion: Inicializa la ventana al centro de la pantalla.
    Retorno: Retorna True
    """
    def centerWindow(self):
        screen = self.frameGeometry()
        ubication = QDesktopWidget().availableGeometry().center()
        screen.moveCenter(ubication)
        self.move(screen.topLeft())