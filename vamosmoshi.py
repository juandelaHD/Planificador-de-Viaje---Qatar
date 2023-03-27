#!/usr/bin/python3
import lectura_archivos as LA
import comandos as com
import sys

rutaPJ = sys.argv[1]
sys.setrecursionlimit(100000)

def main():

    grafo_ciudades, diccionario_ciudades = LA.LeerPJ(rutaPJ)

    while True:
        try:
            entrada = input("")
        except EOFError:
            break
        entrada_completa = entrada.split()
        comando = entrada_completa[0]
        parametros = " ".join(entrada_completa[1:])
        com.leer_entrada(diccionario_ciudades, grafo_ciudades, comando, parametros)

main()