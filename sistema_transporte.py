import heapq
import math

# --- 1. BASE DE CONOCIMIENTO (Reglas de Conexión del Transporte) ---
# Formato: Origen -> [(Destino, Tiempo_en_minutos, Linea_o_Modo)]
BASE_CONOCIMIENTO = {
    'Estacion_A': [('Estacion_B', 5, 'Ruta 1'), ('Estacion_C', 10, 'Ruta 2')],
    'Estacion_B': [('Estacion_A', 5, 'Ruta 1'), ('Estacion_D', 4, 'Ruta 1'), ('Estacion_E', 8, 'Ruta 3')],
    'Estacion_C': [('Estacion_A', 10, 'Ruta 2'), ('Estacion_E', 3, 'Ruta 2')],
    'Estacion_D': [('Estacion_B', 4, 'Ruta 1'), ('Estacion_F', 6, 'Ruta 1')],
    'Estacion_E': [('Estacion_B', 8, 'Ruta 3'), ('Estacion_C', 3, 'Ruta 2'), ('Estacion_F', 2, 'Ruta 3')],
    'Estacion_F': [('Estacion_D', 6, 'Ruta 1'), ('Estacion_E', 2, 'Ruta 3')]
}

# Coordenadas relativas (x, y) para calcular la Heurística h(n)
COORDENADAS = {
    'Estacion_A': (0, 0),
    'Estacion_B': (2, 3),
    'Estacion_C': (5, 1),
    'Estacion_D': (4, 7),
    'Estacion_E': (8, 4),
    'Estacion_F': (10, 8)
}

# --- 2. FUNCIÓN HEURÍSTICA h(n) ---
def heuristica(estacion_actual, estacion_destino):
    x1, y1 = COORDENADAS[estacion_actual]
    x2, y2 = COORDENADAS[estacion_destino]
    # Distancia Euclidiana directa entre coordenadas
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# --- 3. ALGORITMO A* PARA LA MEJOR RUTA ---
def buscar_mejor_ruta(inicio, destino):
    # Lista de prioridad para evaluar los nodos: (f_score, costo_g, nodo_actual, camino)
    cola_prioridad = [(0, 0, inicio, [inicio])]
    visitados = set()

    while cola_prioridad:
        f_score, g_score, actual, camino = heapq.heappop(cola_prioridad)

        if actual == destino:
            return camino, g_score

        if actual in visitados:
            continue
        visitados.add(actual)

        # Regla de inferencia: explorar conexiones desde la base de conocimiento
        for vecino, tiempo, linea in BASE_CONOCIMIENTO.get(actual, []):
            if vecino not in visitados:
                nuevo_g = g_score + tiempo
                nuevo_h = heuristica(vecino, destino)
                nuevo_f = nuevo_g + nuevo_h
                heapq.heappush(cola_prioridad, (nuevo_f, nuevo_g, vecino, camino + [vecino]))

    return None, float('inf')

# --- 4. EJECUCIÓN DEL SISTEMA ---
if __name__ == "__main__":
    origen = 'Estacion_A'
    meta = 'Estacion_F'
    
    ruta, tiempo_total = buscar_mejor_ruta(origen, meta)
    
    print(f"--- MEJOR RUTA DE {origen} A {meta} ---")
    print(f"Ruta encontrada: {' -> '.join(ruta)}")
    print(f"Tiempo total estimado: {tiempo_total} minutos")
