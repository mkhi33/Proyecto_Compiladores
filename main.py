# Importando los modulos de la libreria ply
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


# Obteniendo el contenido desde nustro archivo de entrada



#parser.parse(contenido)

def run():
    test = 'test/prueba1.txt'

    fp = codecs.open(test, "r", "utf-8")
    cadena = fp.read()
    fp.close()
    parser.parse(cadena)



    lexer.input(cadena)
    listaTokens = []

    """
    while True:
        token = lexer.token()
        if not token: break
        listaTokens.append(token)
    return listaTokens, cadena
    """


"""
run()
"""

run()
admin = Administrador('test/prueba1.txt')
cadena = admin.obtenerContenido()
g = Generador(lexer, cadena, resultados)

print(g.dibujarTabla())
