class Ciudad:

    def __init__(self, nombre, coorY, coorX):
        self.nombre = nombre
        self.coorX = coorX
        self.coorY = coorY

    def Obtener_nombre(self):
        return self.nombre

    def ObtenerCoorX(self):
        return self.coorX

    def ObtenerCoorY(self):
        return self.coorY