# Acá debería estar la lógica de lectura de los datos
# de los archivos

import csv

def leer_archivo(ruta):
    """
    Lee el archivo de entrada (CSV con columnas T_i y B_i)
    y devuelve una lista de tuplas (T_i, B_i) como enteros.
    """
    datos = []
    with open(ruta, "r") as f:
        lector = csv.DictReader(f)  # Lee usando el header T_i,B_i
        for fila in lector:
            t = int(fila["T_i"])
            b = int(fila["B_i"])
            datos.append((t, b))
    return datos

