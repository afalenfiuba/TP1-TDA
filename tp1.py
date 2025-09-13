# este es como el main
# aca solo llamamos a las funciones del parser y del greedy

import sys
from src.parser import leer_archivo
from src.greedy import *


def main():
    if len(sys.argv) != 2:
        print("Uso: ruta/a/entrada.txt")
        sys.exit(1) 

    ruta_archivo = sys.argv[1]
    datos = leer_archivo(ruta_archivo)  # [(53,100), (61,100), ...]

    resultado1 = suma_ordenada_por_peso(datos)
    resultado2 = suma_ordenada_por_tiempo(datos)
    resultado3 = suma_ordenada_por_relacion_tiempo_peso(datos)
    resultado4 = suma_ordenada_por_relacion_peso_tiempo(datos)

    print("Suma ponderada ordenada por peso decreciente ", resultado1)
    print("Suma ponderada ordenada por tiempo creciente" ,resultado2)
    print("Suma ponderadas ordenada por relacion t/p creciente", resultado3)
    print("Suma ponderadas ordenada por relacion p/t decreciente", resultado4)


if __name__ == "__main__":
    main()
