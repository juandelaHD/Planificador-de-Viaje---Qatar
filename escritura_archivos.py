from TDAs import grafo, ciudades
import auxiliares as aux

def crear_pajek(grafo, nombre_archivo):
    """Crea un archivo en formato pajek a partir de un grafo."""
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(str(len(grafo.obtener_vertices()))+'\n')
        for ciudad in grafo.obtener_vertices():
            archivo.write(f'{ciudad.Obtener_nombre()},{ciudad.ObtenerCoorX()},{ciudad.ObtenerCoorY()}\n')
        archivo.write(str(len(grafo.obtener_todas_aristas()))+'\n')
        for origen, destino in grafo.obtener_todas_aristas():
            archivo.write(f'{origen.Obtener_nombre()},{destino.Obtener_nombre()},{grafo.obtener_peso(origen, destino)}\n')

def crear_kml(lista, nombre_archivo):
    visitados = set()
    with open(nombre_archivo, 'w') as archivo:
        archivo.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        archivo.write('<kml xmlns="http://earth.google.com/kml/2.1">\n')
        archivo.write('\t<Document>\n')
        archivo.write('\t\t<name>KML</name>\n')
        archivo.write('\n')

        for ciudad in lista:
            if ciudad in visitados:
                continue
            archivo.write('\t\t<Placemark>\n')
            archivo.write(f'\t\t\t<name>{ciudad.Obtener_nombre()}</name>\n')
            archivo.write('\t\t\t<Point>\n')
            archivo.write(f'\t\t\t\t<coordinates>{ciudad.ObtenerCoorX()}, {ciudad.ObtenerCoorY()}</coordinates>\n')
            archivo.write('\t\t\t</Point>\n')
            archivo.write('\t\t</Placemark>\n\n')
            visitados.add(ciudad)

        archivo.write('\n')
        
        for i in range(len(lista)-1):
            origen = lista[i]
            destino = lista[i+1]
            archivo.write('\t\t<Placemark>\n')
            archivo.write('\t\t\t<LineString>\n')
            archivo.write(f'\t\t\t\t<coordinates>{origen.ObtenerCoorX()}, {origen.ObtenerCoorY()} {destino.ObtenerCoorX()}, {destino.ObtenerCoorY()}</coordinates>\n')
            archivo.write('\t\t\t</LineString>\n')
            archivo.write('\t\t</Placemark>\n\n')

        archivo.write('\t</Document>\n')
        archivo.write('</kml>\n')