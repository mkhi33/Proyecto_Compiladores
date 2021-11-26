from nucleo.analizadorLexico import *
import nucleo.ply.ply.lex as lex;
import re
import codecs
import os
import sys

def test():
    test = 'test/prueba1.txt'

    fp = codecs.open(test, "r", "utf-8")
    cadena = fp.read()
    fp.close()

    analizador = lex.lex()
    analizador.input(cadena)


    while True:
        token = analizador.token()
        if not token: break
        print(token)
