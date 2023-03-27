import random

class Grafo:
    """
    Representación del grafo, con sus operaciones básicas.
    """

    def __init__(self, es_dirigido=False):
        """Constructor del grafo vacío"""
        self.vertices = {}
        self.es_dirigido = es_dirigido

    def agregar_vertice(self, vertice):
        """Agrega un vértice al grafo, si no existe."""
        if vertice not in self.vertices:
            self.vertices[vertice] = {}

    def agregar_arista(self, origen, destino, peso=1):
        """Agrega una arista al grafo, si no existe."""
        if origen not in self.vertices:
            self.agregar_vertice(origen)
        if destino not in self.vertices:
            self.agregar_vertice(destino)
        self.vertices[origen][destino] = peso
        if not self.es_dirigido:
            self.vertices[destino][origen] = peso

    def eliminar_vertice(self, vertice):
        """Elimina un vértice del grafo, si existe."""
        if vertice in self.vertices:
            for adyacente in self.vertices[vertice]:
                self.vertices[adyacente].pop(vertice)
            self.vertices.pop(vertice)
    
    def eliminar_arista(self, origen, destino):
        """Elimina una arista del grafo, si existe."""
        if origen in self.vertices and destino in self.vertices[origen]:
            self.vertices[origen].pop(destino)
            if not self.es_dirigido:
                self.vertices[destino].pop(origen)

    def obtener_peso(self, origen, destino):
        """Obtiene el peso de una arista, si existe."""
        if origen in self.vertices and destino in self.vertices[origen]:
            return self.vertices[origen][destino]
        return None

    def obtener_vertices(self):
        """Devuelve una lista con todos los vértices del grafo."""
        return list(self.vertices.keys())
    
    def obtener_todas_aristas(self):
        """Devuelve una lista con todas las aristas del grafo."""
        aristas = []
        for origen in self.vertices:
            for destino in self.vertices[origen]:
                aristas.append((origen, destino))
        return aristas
    
    def obtener_adyacentes(self, vertice):
        """Devuelve una lista con los vértices adyacentes a un vértice."""
        return list(self.vertices[vertice].keys())

    def obtener_vertice_al_azar(self):
        """Devuelve un vértice al azar del grafo."""
        return random.choice(list(self.vertices.keys()))

    def estan_unidos(self, origen, destino):
        """Devuelve True si existe una arista entre origen y destino."""
        return destino in self.vertices[origen]

    def existe_vertice(self, vertice):
        """Devuelve True si el vértice existe en el grafo."""
        return vertice in self.vertices


