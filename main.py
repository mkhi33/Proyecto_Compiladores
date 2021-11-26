# Importando los modulos de la libreria ply
import ply.lex as lex
import ply.yacc as yacc

# importando nuestro analizador lexico 
from nucleo.analizadorLexico import *

#Construcción del analizador lexico
lexer = lex.lex()

# Importando nuestro analizador sintactico
from nucleo.analizadorSintactico import *
parser = yacc.yacc()


# Obteniendo el contenido desde nustro archivo de entrada

archivo = open('./test/prueba1.txt')
contenido = archivo.read()
archivo.close()

print(contenido)

parser.parse(contenido)