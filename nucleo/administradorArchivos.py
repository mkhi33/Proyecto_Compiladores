import codecs
class Administrador:
    def __init__(self, nombreArchivo ):
        self.nombreArchivo = nombreArchivo

    def obtenerContenido(self):
        fp = codecs.open(self.nombreArchivo, "r", "utf-8")
        cadena = fp.read()
        fp.close()
        return cadena
