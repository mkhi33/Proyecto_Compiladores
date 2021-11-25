from nucleo.analizadorLexico import Lexico
import nucleo.ply.ply.lex as lex;
import re
import codecs
import os
import sys


tokens = [
            "ID", "NUMERO", "APARENT", "CPARENT", "SUM", "RES", "MULT", "DIV", "POT", "IGUAL", "PUNTO"
         ]
        
t_APARENT = r'\('
t_CPARENT = r'\('
t_SUM = r'\+'
t_RES = r'-'
t_MULT = r'\*'   
t_DIV = r'/'
t_POT = r'\^' 
t_IGUAL = r'='
t_PUNTO = r'\.'
t_ID = t_ID  = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMERO( t ):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_error( t ):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)



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
