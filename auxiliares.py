from TDAs import grafo, cola, heap

def dfs(grafo, origen):
    visitados = set()
    padres = {}
    _dfs(grafo, origen, visitados, padres)
    return padres

def _dfs(grafo, v, visitados, padres):
    visitados.add(v)
    for w in grafo.obtener_adyacentes(v):
        if w not in visitados:
            padres[w] = v
            _dfs(grafo, w, visitados, padres)

def bfs(grafo, origen):
    visitados = set()
    padres = {}
    _bfs(grafo, origen, visitados, padres)
    return padres

def _bfs(grafo, origen, visitados, padres):
    q = cola.Cola()
    q.encolar(origen)
    visitados.add(origen)
    while not q.esta_vacia():
        v = q.desencolar()
        for w in grafo.obtener_adyacentes(v):
            if w not in visitados:
                padres[w] = v
                visitados.add(w)
                q.encolar(w)

def calcular_grados_entrada(grafo):
    grados = {}
    for v in grafo.obtener_vertices():
        grados[v] = 0
    for v in grafo.obtener_vertices():
        for w in grafo.obtener_adyacentes(v):
            grados[w] += 1
    return grados

def calcular_grados_salida(grafo):
    grados = {}
    for v in grafo.obtener_vertices():
        grados[v] = len(grafo.obtener_adyacentes(v))
    return grados

def es_conexo(grafo):
    visitados = set()
    _dfs(grafo, grafo.obtener_vertices()[0], visitados, {})
    return len(visitados) == len(grafo.obtener_vertices())

def peso_total(grafo):
    peso = 0
    visitados = set()
    for v in grafo.obtener_vertices():
        for w in grafo.obtener_adyacentes(v):
            if (v, w) not in visitados and (w, v) not in visitados:
                peso += grafo.obtener_peso(v, w)
                visitados.add((v, w))
                visitados.add((w, v))
    return peso

# ORDEN TOPOLOGICO -------------------------------------------------------

def orden_topologico(grafo):
    grados = calcular_grados_entrada(grafo)
    orden = []
    q = cola.Cola()
    for v in grafo.obtener_vertices():
        if grados[v] == 0:
            q.encolar(v)
    while not q.esta_vacia():
        v = q.desencolar()
        orden.append(v)
        for w in grafo.obtener_adyacentes(v):
            grados[w] -= 1
            if grados[w] == 0:
                q.encolar(w)
    return orden

# CAMINO MINIMO -----------------------------------------------------------

def camino_minimo(grafo, origen):
    distancias = {}
    padres = {}
    for v in grafo.obtener_vertices():
        distancias[v] = float("inf")
    distancias[origen] = 0
    padres[origen] = None
    cola = heap.Heap(cmp)
    cola.encolar((origen, 0))
    while not cola.esta_vacia():
        v, _ = cola.desencolar()
        for w in grafo.obtener_adyacentes(v):
            distancia_por_aca = distancias[v] + grafo.obtener_peso(v, w)
            if distancia_por_aca < distancias[w]:
                padres[w] = v
                distancias[w] = distancia_por_aca
                cola.encolar((w, distancias[w]))
    return padres, distancias

def reconstruir_camino(origen, destino, padres, distancias):
    if distancias[destino] == float("inf"):
        return None
    camino = []
    v = destino
    while v != origen:
        camino.append(v)
        v = padres[v]
    camino.append(origen)
    camino.reverse()
    return camino

# MST ---------------------------------------------------------------------
def cmp(a, b):
    if a[1] < b[1]:
        return 1
    elif a[1] > b[1]:
        return -1
    else:
        return 0

def arbol_tendido_minimo(grafo_original):
    nuevo = grafo.Grafo()
    for v in grafo_original.obtener_vertices():
        nuevo.agregar_vertice(v)
    cola = heap.Heap(cmp)
    visitados = set()
    
    v = grafo_original.obtener_vertice_al_azar()
    for w in grafo_original.obtener_adyacentes(v):
        cola.encolar((v, grafo_original.obtener_peso(v, w), w))

    while not cola.esta_vacia():
        v, peso, w = cola.desencolar()
        if w not in visitados:
            nuevo.agregar_arista(v, w, peso)
            visitados.add(w)
            for x in grafo_original.obtener_adyacentes(w):
                if x not in visitados:
                    cola.encolar((w, grafo_original.obtener_peso(w, x), x))
    return nuevo

# EULER -------------------------------------------------------------------

def euleriano(grafo, vertice):
    if not es_conexo(grafo):
        return None
    impares = vertices_impares(grafo)
    if impares == 0:
        return hierholzer(grafo, vertice)
    return  None

def vertices_impares(grafo):
    cant_vertices_impares = 0
    grados = calcular_grados_salida(grafo)
    for grado in grados.values():
        if grado % 2 != 0:
            cant_vertices_impares += 1
    return cant_vertices_impares

# HIERHOLZER -------------------------------------------------------------

def hierholzer(grafo, vertice):
    visitados = set()
    ciclo = _hierholzer(grafo, visitados, vertice, [])
    completo = completar_caminos(grafo, ciclo, visitados)
    if completo[0] != completo[-1]:
        completo = completar_caminos(grafo, completo, visitados)
    return completo

def _hierholzer(grafo, visitados, v, ciclo):
    ciclo.append(v)
    for w in grafo.obtener_adyacentes(v):
        if (v, w) not in visitados or (w, v) not in visitados:
            visitados.add((v, w))
            visitados.add((w, v))
            return _hierholzer(grafo, visitados, w, ciclo) 
    # ya tenemos el ciclo cerrado
    return ciclo

def completar_caminos(grafo, ciclo, visitados):
    for v in range(len(ciclo)-1):
        for w in grafo.obtener_adyacentes(ciclo[v]):
            if (ciclo[v], w) not in visitados or (w, ciclo[v]) not in visitados:
                nuevo_ciclo = _hierholzer(grafo, visitados, ciclo[v], [])
                ciclo = ciclo[:v] + nuevo_ciclo + ciclo[v+1:]
    return ciclo
