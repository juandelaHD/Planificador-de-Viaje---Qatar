import auxiliares as aux
import lectura_archivos as r
import escritura_archivos as w

def leer_entrada(dicc_ciudades, grafo, comando, parametros):

    if comando == "reducir_caminos":
        archivo_pj = parametros
        reducir_caminos(grafo, archivo_pj)

    if comando == "viaje":
        parametros = parametros.split(",")
        origen = parametros[0]
        if origen not in dicc_ciudades:
            print("No se encontro recorrido")
            return
        archivo_kml = parametros[1][1:]
        tomar_toda_ruta(grafo, origen, archivo_kml, dicc_ciudades)

    if comando == "ir":
        parametros = parametros.split(",")
        origen = parametros[0]
        destino = parametros[1][1:]
        archivo_kml = parametros[2][1:]
        if origen not in dicc_ciudades or destino not in dicc_ciudades:
            print("No se encontro recorrido")
            return
        viajar(grafo, dicc_ciudades, origen, destino, archivo_kml)

    if comando == "itinerario":
        archivo_csv = parametros
        recomendar_itinerario(dicc_ciudades, grafo, archivo_csv)


def imprimir_caminos(camino):
    resultado = ""
    for ciudad in camino:
        resultado += ciudad.Obtener_nombre() + " -> "
    resultado = resultado[:-4]
    print(resultado)


def reducir_caminos(grafo, nombre_archivo):
    mst = aux.arbol_tendido_minimo(grafo)
    w.crear_pajek(mst, nombre_archivo)
    print(f'Peso total: {aux.peso_total(mst)}')


def tomar_toda_ruta(grafo, origen, nombre_archivo, dicc_ciudades):
    camino = aux.euleriano(grafo, dicc_ciudades[origen])
    if camino is None:
        print("No se encontro recorrido")
        return
    imprimir_caminos(camino)
    tiempo_total = 0
    for index in range(len(camino)-1):
        tiempo_total += grafo.obtener_peso(camino[index], camino[index+1])
    print(f'Tiempo total: {tiempo_total}')
    w.crear_kml(camino, nombre_archivo)


def recomendar_itinerario(dicc_ciudades, grafo, nombre_archivo):
    grafo_recomendaciones = r.leer_recomendaciones(dicc_ciudades, grafo, nombre_archivo)
    orden = aux.orden_topologico(grafo_recomendaciones)
    if len(orden) < len(grafo_recomendaciones.obtener_vertices()):
        print("No se encontro recorrido")
        return
    imprimir_caminos(orden)


def viajar(grafo, dicc_ciudades, origen, destino, nombre_archivo):
    padres, tiempos = aux.camino_minimo(grafo, dicc_ciudades[origen])
    camino = aux.reconstruir_camino(dicc_ciudades[origen], dicc_ciudades[destino], padres, tiempos)
    if camino is None:
        print("No se encontro recorrido")
        return
    imprimir_caminos(camino)
    print(f'Tiempo total: {tiempos[dicc_ciudades[destino]]}')
    w.crear_kml(camino, nombre_archivo)

