# la implementacion del algoritmo greedy del problema

def suma_ordenada_por_peso(batallas):
    batallas_ordenadas = sorted(batallas, key=lambda x: x[1], reverse=True)

    suma_total = 0
    suma_tiempos = 0
    for t_i, p_i in batallas_ordenadas:
        suma_tiempos = t_i + suma_tiempos
        suma_total = (p_i * suma_tiempos) + suma_total

    return suma_total


def suma_ordenada_por_tiempo(batallas):
    ordenados = sorted(batallas, key=lambda x: x[0])

    suma_total = 0
    suma_tiempos = 0
    for t_i, p_i in ordenados:
        suma_tiempos = t_i + suma_tiempos
        suma_total = (p_i * suma_tiempos) + suma_total

    return suma_total


def suma_ordenada_por_relacion_tiempo_peso(batallas):
    # Calculamos tiempo/peso
    ordenados_por_relacion = sorted(batallas, key=lambda x: x[0] / x[1])
    suma_total = 0
    suma_tiempos = 0
    for t_i, p_i in ordenados_por_relacion:
        suma_tiempos = t_i + suma_tiempos
        suma_total = (p_i * suma_tiempos) + suma_total

    return suma_total

def suma_ordenada_por_relacion_peso_tiempo(batallas):
    # Calculamos peso/tiempo decreciente
    ordenados_por_relacion = sorted(batallas, key=lambda x: x[1] / x[0], reverse=True)
    suma_total = 0
    suma_tiempos = 0
    for t_i, p_i in ordenados_por_relacion:
        suma_tiempos = t_i + suma_tiempos
        suma_total = (p_i * suma_tiempos) + suma_total

    return suma_total