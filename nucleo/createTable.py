import math
class CreateTable:
    """
    Esta clase contiene la logíca para crear una tabla ASCII, el usuario no tendria que modificar codigo, excepto
    que desee mejorarlo.
    """
    def __init__(self, header, footer, rows, intColumns):
        """
        :param header: Título de la tabla.
        :param rows: Todas las filas que componen la tabla. (Lista de listas) [[col1, col2, ...], [col1, col2 ...], ...]
        :param intColumns: Número de columnas que contiene la tabla.
        """
        self.__header = header
        self.__footer = footer
        self.__rows = rows
        self.__intColumns = intColumns
        self.__dicHighs = {}
        self.tab = 4
        self.__width = 0

    def initDicHighs(self):
        """
        Esta función inicializa el diccionario dicHighs en 0.
        :return: booleano
        """
        for i in range(self.__intColumns):
            self.__dicHighs[i] = 0
        return True

    def getStrHighs(self):
        """
        Esta función obtiene el tamaño de las cadenas mas grande en cada columna y lo almacena en un diccionario
        (self.__dicHighs)
        :return: booleano
        """
        self.initDicHighs()
        for i in range(len(self.__rows)):
            for j in range(len(self.__rows[i])):
                if self.__dicHighs[j] < len(str(self.__rows[i][j])):
                    self.__dicHighs[j] = len(str(self.__rows[i][j]))
        return True


    def getBodyArray(self):
        """
        Esta función obtiene el cuerpo de la tabla, con sus espaciados correspondientes y los almacena en una lista.
        :return: Retorna una lista con el contenido del cuerpo de la tabla.
        """
        content = []
        for row in self.__rows:
            colIndex = 0
            column = []
            for item in row:
                element = self.formattedElement(item, colIndex)
                column.append(element)
                colIndex +=1
            content.append(column)
        self.__width = self.getWidth(content[0])
        return content

    def getWidth(self, row):
        """
        :param row: fila[i] de la tabla
        :return: retorna la anchura de la tabla, sin incluir los espacios.
        """
        count = 0
        for col in row:
            count += len(col)
        return count


    def getHeaderArray(self):
        """
        Esta función obtiene el encabezado o título de la tabla.
        :return: Retorna una lista con el título de la tabla y sus espacios correspondientes.
        """

        spaces = math.ceil(self.__width/2 - len(self.__header)/2)
        return ["%s%s%s"%(" "*spaces, self.__header, " "*spaces)]
    def getFooterArray(self):
        """
        Esta función obtiene el footer o pie de la tabla.
        :return: Retorna una lista con el footer de la tabla y sus espacios correspondientes.
        """

        spaces = math.ceil(self.__width/2 - len(self.__footer)/2)
        return ["%s%s%s"%(" "*spaces, self.__footer, " "*spaces)]



    def formattedElement(self, item, colIndex):
        """
        Esta función da formato a la tabla con sus respectivos elementos.
        :param item: Elemento[i] de una fila
        :param colIndex: posición de la columna dentro de la fila.
        :return: (str) retorna el elemento con los espacios correspondientes.
        """
        spaces = self.__dicHighs[colIndex]+ self.tab - len(str(item))
        return "|%s%s"%(item," "*spaces)


    def createTable(self):
        """
        Esta función crea la tabla, es la unica función que el usuario deberia de llamar.
            1. inicializar en 0 el diccionario de los maximis string.
            2. Obtener las cadenas maximas de cada columna y asignarlos al diccionario de los maximos string.
            3. Obtener el cuerpo o contenido de la tabla.
            4. Obtener el título de la tabla.
            5. Definimos lineas que separan renglones.
            6. Agregamos el contenido a una cadena de texto agregando sus decoraciones.
        :return: (str) retorna una cadena de texto con un dibujo de tabla.
        """
        self.initDicHighs()
        self.getStrHighs()
        body = self.getBodyArray()
        header = self.getHeaderArray()

        lines = "%s\n"%("-"* len("".join(header)))

        content= "%s%s\n%s"%(lines,"".join(header),lines)
        for row in body:
            content += "%s|"% "".join(row)
            content += "\n%s"%lines
        footer = self.getFooterArray()
        content += content.join(footer)
        return content