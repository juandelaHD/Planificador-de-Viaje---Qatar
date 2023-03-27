from TDAs import grafo, ciudades
import csv

def LeerPJ(ruta):
    grafo_ciudades = grafo.Grafo()
    dicc = {}
    with open(ruta) as archivo:

        # Colocamos ciudades (vertices)
        contador = int(archivo.readline())
        for _ in range(contador):
            nombre, x, y = archivo.readline().rstrip().split(",")
            ciudad = ciudades.Ciudad(nombre, y, x)
            dicc[nombre] = ciudad
            grafo_ciudades.agregar_vertice(ciudad)
        
        # Colocamos rutas (aristas)
        contador = int(archivo.readline())
        for _ in range(contador):
            origen, destino, tiempo = archivo.readline().rstrip().split(",")
            grafo_ciudades.agregar_arista(dicc[origen], dicc[destino], int(tiempo))

    return grafo_ciudades, dicc

def leer_recomendaciones(dicc_ciudades, grafo_original, ruta_csv):
    grafo_recomendaciones = grafo.Grafo(es_dirigido=True)
    for ciudad in grafo_original.obtener_vertices():
        grafo_recomendaciones.agregar_vertice(ciudad)
    with open(ruta_csv) as archivo:
        lector = csv.reader(archivo, delimiter=',')
        for fila in lector:
            origen = dicc_ciudades[fila[0]]
            destino = dicc_ciudades[fila[1]]
            grafo_recomendaciones.agregar_arista(origen, destino)
    return grafo_recomendaciones
