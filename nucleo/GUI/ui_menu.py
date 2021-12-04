
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QColorDialog
from nucleo.pantallas.GUI_Menu import Ui_MainWindow

from nucleo.GUI.ui_acercaDe import GuiAcercaDe
from nucleo.GUI.ui_calculadora import GuiCalculadora
from nucleo.GUI.ui_archivos import UiDialogFile
from nucleo.GUI.ui_dialogo import GUIDialogo

import ply.lex as lex
import ply.yacc as yacc
import codecs

from nucleo.generSalida import Generador
from nucleo.administradorArchivos import Administrador

# importando nuestro analizador lexico 
from nucleo.analizadorLexico import *

#Construcción del analizador lexico
lexer = lex.lex()

# Importando nuestro analizador sintactico
from nucleo.analizadorSintactico import *
parser = yacc.yacc()


class GUIMenu(QMainWindow):
    def __init__(self, parent = None):

        super(GUIMenu, self).__init__(parent)
     
        self.uiMenu = Ui_MainWindow()
        self.uiMenu.setupUi(self)
        self.cadena = ""

        

        # Instanciar las demás ventanas
        self.uiAcercaDe = GuiAcercaDe()
        self.uiCalculadora = GuiCalculadora()
        self.uiFileDialog = UiDialogFile()
        self.uiDialogo = GUIDialogo()


        self.limpiarPantalla = False

        # Eventos de botones

        self.uiMenu.btnAcercaDe.clicked.connect(self.mostrarAcercaDe)
        self.uiMenu.btnSalir.clicked.connect(self.salir)
        self.uiMenu.btnCalculadora.clicked.connect(self.mostrarCalculadora)

        # Eventos de botones en calculadora
        self.uiCalculadora.uiCalculadora.pushButton.clicked.connect(self.openDialogFileOrigin)

        self.uiCalculadora.uiCalculadora.lblEntrada.setText('')
        self.uiCalculadora.uiCalculadora.lcdEntrada.setProperty("value", 0)
        self.uiCalculadora.uiCalculadora.pushButton_2.clicked.connect(self.dibujarTabla)


        self.uiCalculadora.uiCalculadora.btn1.clicked.connect(self.click1)
        self.uiCalculadora.uiCalculadora.btn2.clicked.connect(self.click2)
        self.uiCalculadora.uiCalculadora.btn3.clicked.connect(self.click3)
        self.uiCalculadora.uiCalculadora.btn4.clicked.connect(self.click4)
        self.uiCalculadora.uiCalculadora.btn5.clicked.connect(self.click5)
        self.uiCalculadora.uiCalculadora.btn6.clicked.connect(self.click6)
        self.uiCalculadora.uiCalculadora.btn7.clicked.connect(self.click7)
        self.uiCalculadora.uiCalculadora.btn8.clicked.connect(self.click8)
        self.uiCalculadora.uiCalculadora.btn9.clicked.connect(self.click9)
        self.uiCalculadora.uiCalculadora.btn0.clicked.connect(self.click0)
        self.uiCalculadora.uiCalculadora.btnDecimal.clicked.connect(self.clickPunto)

        self.uiCalculadora.uiCalculadora.btnSum.clicked.connect(self.clickSum)
        self.uiCalculadora.uiCalculadora.btnRes.clicked.connect(self.clickRes)
        self.uiCalculadora.uiCalculadora.btnMult.clicked.connect(self.clickMul)
        self.uiCalculadora.uiCalculadora.btnDiv.clicked.connect(self.clickDiv)
        self.uiCalculadora.uiCalculadora.btnPot.clicked.connect(self.clickPot)
        self.uiCalculadora.uiCalculadora.btnIgual.clicked.connect(self.clickIgual)

        self.uiCalculadora.uiCalculadora.btnAPAR.clicked.connect(self.clickAPAR)
        self.uiCalculadora.uiCalculadora.btnCPAR.clicked.connect(self.clickCPAR)
        self.uiCalculadora.uiCalculadora.btnLimpiar.clicked.connect(self.clickLimpiar)

        self.uiDialogo.uiDialogo.pushButton.clicked.connect(self.uiDialogo.close)

    

    def mostrarAcercaDe(self):
        self.uiAcercaDe.show()

    def mostrarCalculadora(self):
        self.uiCalculadora.show()

    def salir(self):
        self.close()

    def openDialogFileOrigin(self):
        files = self.uiFileDialog.openFileNamesDialog()
        if(files):
            adminArchivos = Administrador(files)
            contenido = adminArchivos.obtenerContenido()
            parser.parse(contenido)
            self.uiDialogo.show()
            self.dibujarTabla(contenido)
            
        else:
            print("No se selecciono ningun archivo")

    def actualizarCalculadora(self):
        self.uiCalculadora.uiCalculadora.lcdEntrada.setProperty("value", 26.26)

    def actualizarLblEntrada(self, valor):
        valorActual = self.uiCalculadora.uiCalculadora.lblEntrada.text()

        nuevoValor =  "%s%s"%(valorActual, valor)

        self.uiCalculadora.uiCalculadora.lblEntrada.setText(nuevoValor)

    def calcular(self):

        if self.limpiarPantalla :
            self.uiCalculadora.uiCalculadora.lcdEntrada.setProperty("value", 0.0)
            self.limpiarPantalla = False
        try:
            expresion = "OPERAR[%s]$"%(self.uiCalculadora.uiCalculadora.lblEntrada.text())
            parser.parse(expresion)
            resultado = operacion["OPERAR"]
            if(isinstance(resultado, (int, float, str))):
                if(resultado):
                    self.cadena += "%s\n"%expresion
                    self.uiCalculadora.uiCalculadora.lcdEntrada.setProperty("value", float(resultado))
                    self.limpiarPantalla = True
        except:
            print("Ocurrio un error")

    def dibujarTabla(self, cadena = None):
        if not cadena: cadena = self.cadena
        g = Generador(lexer, cadena, resultados)
        contenido = g.dibujarTabla()
        self.uiDialogo.show()
        print(contenido)
       

    def click1(self):
        self.actualizarLblEntrada('1')
    def click2(self):
        self.actualizarLblEntrada('2')
    def click3(self):
        self.actualizarLblEntrada('3')
    def click4(self):
        self.actualizarLblEntrada('4')
    def click5(self):
        self.actualizarLblEntrada('5')
    def click6(self):
        self.actualizarLblEntrada('6')
    def click7(self):
        self.actualizarLblEntrada('7')
    def click8(self):
        self.actualizarLblEntrada('8')
    def click9(self):
        self.actualizarLblEntrada('9')
    def click0(self):
        self.actualizarLblEntrada('0')
    def clickPunto(self):
        self.actualizarLblEntrada('.')

    def clickSum(self):
        self.actualizarLblEntrada("+")
    def clickRes(self):
        self.actualizarLblEntrada("-")
    def clickMul(self):
        self.actualizarLblEntrada("*")
    def clickDiv(self):
        self.actualizarLblEntrada("/")
    def clickIgual(self):
        #self.actualizarLblEntrada("=")
        self.calcular()
        self.uiCalculadora.uiCalculadora.lblEntrada.setText("")

    def clickPot(self):
        self.actualizarLblEntrada("^")
    
    def clickAPAR(self):
        self.actualizarLblEntrada("(")
    def clickCPAR(self):
        self.actualizarLblEntrada(")")
    def clickLimpiar(self):
        self.uiCalculadora.uiCalculadora.lblEntrada.setText("")
        self.uiCalculadora.uiCalculadora.lcdEntrada.setProperty("value", 0)
        error = None
