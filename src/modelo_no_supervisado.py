import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import time

def ejecutar_clustering():
    # 1. Cargar el dataset existente de transporte
    df = pd.read_csv('data/dataset_transporte.csv')
    
    # 2. Seleccionar características numéricas para el agrupamiento no supervisado
    X = df[['Pasajeros_Estimados', 'Ocupacion_Bus_Porcentaje']]
    
    # 3. Normalizar / Escalar los datos (Requerido para K-Means)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # 4. Aplicar el algoritmo K-Means (Capítulo 16: Técnicas de Agrupamiento)
    inicio = time.perf_counter()
    # Agrupamos en 3 clusters operativos (ej: Baja, Media, Alta congestión)
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(X_scaled)
    fin = time.perf_counter()
    
    tiempo_ms = (fin - inicio) * 1000
    
    # 5. Mostrar resultados en consola
    print("\n==================================================")
    print(" MODELO NO SUPERVISADO - K-MEANS (AGRUPAMIENTO)")
    print("==================================================")
    print(f" Tiempo de ejecución: {tiempo_ms:.4f} ms")
    print(f" Cantidad de clusters: 3")
    print(f"\nCentros de los clusters (en valores normalizados):\n{kmeans.cluster_centers_}\n")
    
    print("--- DISTRIBUCIÓN DE REGISTROS POR CLUSTER ---")
    conteo_clusters = df['Cluster'].value_counts().sort_index()
    for cluster_id, cantidad in conteo_clusters.items():
        print(f" Cluster {cluster_id}: {cantidad} registros asignados")
        
    print("==================================================\n")
    
    # 6. Guardar un nuevo dataset con los clusters asignados
    df.to_csv('data/dataset_con_clusters.csv', index=False)
    print("Dataset con clusters guardado en 'data/dataset_con_clusters.csv'")

if __name__ == "__main__":
    ejecutar_clustering()