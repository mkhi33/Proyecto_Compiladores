from nucleo.tableAscci import TableAscii
class Generador:
    def __init__(self, lexer, cadena,resultados):
        self.lexer = lexer
        self.cadena = cadena
        self.resultados = resultados

    def obtenerListaTokens(self):
        lista = []
        self.lexer.input(self.cadena)
        listaTokens = []

        while True:
            token = self.lexer.token()
            lista.append(token)
            if not token: break
        return lista

    
    
    def obtenerContenidoTabla(self):
        instrucciones = self.cadena.split('\n')
        tokens = self.obtenerListaTokens()
        filas = []

        for token in tokens:
            lista = str(token).strip('LexToken(')[:-1].split(",")
            if(len(lista) == 4 ):
                data = { "nombre": lista[0], "token": lista[1], "linea":lista[2], "inicio":lista[3],    }
                filas.append(data)

        return filas
    
    def obtenerTablas(self):
        instrucciones = self.cadena.split('\n')
        contenido = self.obtenerContenidoTabla()
        
        listaTablas = []
        res = ""

        table = TableAscii(4)

        columna1 = [ "Nombre", "Token", "Linea", "Inicio" ]
        table.addRow(columna1)
        conta = 0
        for elemento in contenido:
        
            columna = [ elemento["nombre"], elemento["token"], elemento["linea"], elemento["inicio"] ]
            table.addRow(columna)
            if(elemento["token"].strip('\'') == "$"):
                res += "\n%s = %s"%(instrucciones[conta], self.resultados[conta][0])
               
                table.addFooter("Resultado: %s"%self.resultados[conta][0])

                table.addHeader("Instrucción: %s"%instrucciones[conta])
                listaTablas.append(table)
                table = TableAscii(4)
                table.addRow(columna1)
                conta +=1
        return listaTablas, res
        

    def dibujarTabla(self):
        try:

            tablas , res = self.obtenerTablas()
            contenido ="\n*********************\n Analizador Léxico\n *********************\n"

            for tabla in tablas:
                contenido += "\n%s\n"%(tabla.getTable())


            # Mostrando las respuestas

            contenido += res


            archivo = open('salida.txt', "w")
            archivo.write(contenido)
            archivo.close()
            return contenido

        except:
            print("No se pudo generar la tabla")


        