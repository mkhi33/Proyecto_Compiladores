from nucleo.createTable import CreateTable

class TableAscii:
    def __init__(self, columns):
        """
        :param columns: numero de columnas que contendra la tabla
        """
        self.__intColumns = columns
        self.__row = []
        self.__header = ""
        self.__footer = ""


    def addRow(self, col = []):
        """
        :param col: Lista con los elementos de una fila ejemplo: ["Elemento 1", "Elemento 2", "Elemento 3" ...]
        :return: Boleano
        """
        if isinstance(col,list):
            if(len(col) == self.__intColumns):
                self.__row.append(col)
                return True
            return False
        return False
    def addHeader(self, header):
        """
        :param header: Título que tendra la tabla
        :return: Boleano
        """
        self.__header = header
        return True

    def addFooter(self, footer):
        self.__footer = footer
        return True

    def getTable(self):
        """
        :return: retorna la tabla en una cadena de texto.
        """
        table = CreateTable(self.__header, self.__footer, self.__row, self.__intColumns)
        return table.createTable()