import heapq
import math
import time  # <--- 1. Importar el módulo time
import argparse
import sys

# --- BASE DE CONOCIMIENTO Y COORDENADAS ---
BASE_CONOCIMIENTO = {
    'Estacion_A': [('Estacion_B', 5, 'Ruta 1'), ('Estacion_C', 10, 'Ruta 2')],
    'Estacion_B': [('Estacion_A', 5, 'Ruta 1'), ('Estacion_D', 4, 'Ruta 1'), ('Estacion_E', 8, 'Ruta 3')],
    'Estacion_C': [('Estacion_A', 10, 'Ruta 2'), ('Estacion_E', 3, 'Ruta 2')],
    'Estacion_D': [('Estacion_B', 4, 'Ruta 1'), ('Estacion_F', 6, 'Ruta 1')],
    'Estacion_E': [('Estacion_B', 8, 'Ruta 3'), ('Estacion_C', 3, 'Ruta 2'), ('Estacion_F', 2, 'Ruta 3')],
    'Estacion_F': [('Estacion_D', 6, 'Ruta 1'), ('Estacion_E', 2, 'Ruta 3')]
}

COORDENADAS = {
    'Estacion_A': (0, 0),
    'Estacion_B': (2, 3),
    'Estacion_C': (5, 1),
    'Estacion_D': (4, 7),
    'Estacion_E': (8, 4),
    'Estacion_F': (10, 8)
}

def heuristica(estacion_actual, estacion_destino):
    x1, y1 = COORDENADAS[estacion_actual]
    x2, y2 = COORDENADAS[estacion_destino]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def buscar_mejor_ruta(inicio, destino):
    cola_prioridad = [(0, 0, inicio, [inicio])]
    visitados = set()

    while cola_prioridad:
        f_score, g_score, actual, camino = heapq.heappop(cola_prioridad)

        if actual == destino:
            return camino, g_score

        if actual in visitados:
            continue
        visitados.add(actual)

        for vecino, tiempo, linea in BASE_CONOCIMIENTO.get(actual, []):
            if vecino not in visitados:
                nuevo_g = g_score + tiempo
                nuevo_h = heuristica(vecino, destino)
                nuevo_f = nuevo_g + nuevo_h
                heapq.heappush(cola_prioridad, (nuevo_f, nuevo_g, vecino, camino + [vecino]))

    return None, float('inf')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sistema Inteligente de Transporte Masivo - Algoritmo A*")
    parser.add_argument('--origen', type=str, default='Estacion_A', help='Estación de partida')
    parser.add_argument('--destino', type=str, default='Estacion_F', help='Estación de llegada')
    
    args = parser.parse_args()
    origen = args.origen
    meta = args.destino

    # --- 2. MEDIR TIEMPO DE EJECUCIÓN ---
    inicio_tiempo = time.perf_counter()  # Marca de tiempo de inicio
    
    ruta, tiempo_total = buscar_mejor_ruta(origen, meta)
    
    fin_tiempo = time.perf_counter()    # Marca de tiempo de fin
    
    tiempo_ejecucion_ms = (fin_tiempo - inicio_tiempo) * 1000  # Convertir a milisegundos

    # --- 3. MOSTRAR RESULTADOS ---
    if ruta:
        print(f"\n==========================================")
        print(f" MEJOR RUTA ENCONTRADA (Algoritmo A*)")
        print(f"==========================================")
        print(f" Origen:            {origen}")
        print(f" Destino:           {meta}")
        print(f" Ruta:              {' -> '.join(ruta)}")
        print(f" Tiempo del viaje:  {tiempo_total} minutos")
        print(f" Tiempo algoritmo:  {tiempo_ejecucion_ms:.4f} ms")
        print(f"==========================================\n")
    else:
        print(f"No se encontró una ruta válida entre {origen} y {meta}.")
