import nucleo.ply.ply.lex as lex;
import re
import codecs
import os
import sys

class Lexico:
    def __init__(self):
        self.tokens = [
            "ID", "NUMERO", "APARENT", "CPARENT", "SUM", "RES", "MULT", "DIV", "POT", "IGUAL", "PUNTO"
         ]
        
        self.t_APARENT = r'\('
        self.t_CPARENT = r'\('
        self.t_SUM = r'\+'
        self.t_RES = r'-'
        self.t_MULT = r'\*'   
        self.t_DIV = r'/'
        self.t_POT = r'\^' 
        self.t_IGUAL = r'='
        self.t_PUNTO = '.'
        self.t_ID = t_ID  = r'[a-zA-Z_][a-zA-Z0-9_]*'


        
    def t_NUMERO( self, t ):
        r'\d+'
        try:
            t.value = int(t.value)
        except ValueError:
            print("Integer value too large %d", t.value)
            t.value = 0
        return t

    def t_error( self, t ):
        print("Caracter ilegal '%s'" % t.value[0])
        t.lexer.skip(1)

    def run(self):

        l = Lexico()

        analizador = lex.lex()

        test = 'test/prueba1.txt'

        fp = codecs.open(test, "r", "utf-8")
        cadena = fp.read()
        fp.close()

        analizador.input(cadena)


        while True:
            token = analizador.token()
            if not token: break
            print(token)