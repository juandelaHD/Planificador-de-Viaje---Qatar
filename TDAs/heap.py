class Heap:

    def __init__(self, cmp):
        self.datos = []
        self.cant = 0
        self.cmp = cmp

    def esta_vacia(self):
        return self.cant == 0

    def VerMax(self):
        if self.cant == 0:
            return None
        return self.datos[0]

    def encolar(self, dato):
        self.datos.append(dato)
        self.cant += 1
        self.upheap(self.cant - 1)

    def upheap(self, pos):
        if pos > 0:
            padre = (pos - 1) // 2
            if self.cmp(self.datos[padre], self.datos[pos]) < 0:
                self.datos[padre], self.datos[pos] = self.datos[pos], self.datos[padre]
                self.upheap(padre)

    def desencolar(self):
        if self.cant == 0:
            return None
        dato = self.datos[0]
        self.cant -= 1
        self.datos[0] = self.datos[self.cant]
        self.datos = self.datos[:self.cant]
        self.downheap(0)
        return dato

    def downheap(self, pos):
        hijo_izq = 2 * pos + 1
        hijo_der = 2 * pos + 2
        if hijo_izq < self.cant:
            if hijo_der < self.cant:
                if self.cmp(self.datos[hijo_izq], self.datos[hijo_der]) > 0:
                    hijo_max = hijo_izq
                else:
                    hijo_max = hijo_der
            else:
                hijo_max = hijo_izq
            if self.cmp(self.datos[pos], self.datos[hijo_max]) < 0:
                self.datos[pos], self.datos[hijo_max] = self.datos[hijo_max], self.datos[pos]
                self.downheap(hijo_max)