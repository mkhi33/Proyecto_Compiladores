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

class Calculadora:
    def __init__(self, expresion):
        self.expresion = expresion
    
    def calcular(self):
        parser.parse(self.expresion)
