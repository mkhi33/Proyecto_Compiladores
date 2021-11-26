
# Analizador lexico

tokens = [
            "OPERAR", "NUMERO", "APARENT", "CPARENT", "SUM", "RES", "MULT", "DIV", "POT", "DECIMAL", "ACOR", "CCOR", "FINAL"
         ]
        
t_OPERAR = "OPERAR"
t_APARENT = r'\('
t_CPARENT = r'\)'
t_ACOR = r'\['
t_CCOR = r'\]'
t_SUM = r'\+'
t_RES = r'-'
t_MULT = r'\*'   
t_DIV = r'/'
t_POT = r'\^' 
t_FINAL = r'\$'
t_ignore = " \t"



def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t

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

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


