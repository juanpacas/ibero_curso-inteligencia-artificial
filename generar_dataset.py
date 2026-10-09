import pandas as pd
import numpy as np

# Configuración de semilla para reproducibilidad
np.random.seed(42)
n_muestras = 500

estaciones = ['San_Mateo', 'Terreros', 'Bosa', 'Portal_Sur', 'General_Santander', 'Ricaurte', 'Calle_72']
dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
clima = ['Despejado', 'Lluvia_Ligera', 'Lluvia_Intensa']

data = {
    'Hora_Pico': np.random.choice([1, 0], size=n_muestras, p=[0.4, 0.6]),
    'Dia_Semana': np.random.choice(dias, size=n_muestras),
    'Clima': np.random.choice(clima, size=n_muestras, p=[0.6, 0.3, 0.1]),
    'Pasajeros_Estimados': np.random.randint(50, 500, size=n_muestras),
    'Incidente_Vial': np.random.choice([1, 0], size=n_muestras, p=[0.15, 0.85]),
    'Ocupacion_Bus_Porcentaje': np.random.randint(30, 100, size=n_muestras)
}

df = pd.DataFrame(data)

# Regla lógica para determinar el Nivel de Retraso (Variable Objetivo / Label)
def calcular_retraso(row):
    puntos = 0
    if row['Hora_Pico'] == 1: puntos += 3
    if row['Clima'] == 'Lluvia_Intensa': puntos += 3
    elif row['Clima'] == 'Lluvia_Ligera': puntos += 1
    if row['Incidente_Vial'] == 1: puntos += 4
    if row['Ocupacion_Bus_Porcentaje'] > 85: puntos += 2
    
    if puntos >= 6:
        return 'Alto'
    elif puntos >= 3:
        return 'Medio'
    else:
        return 'Bajo'

df['Nivel_Retraso'] = df.apply(calcular_retraso, axis=n_muestras if False else 1)

# Guardar dataset
df.to_csv('data/dataset_transporte.csv', index=False)
print("Dataset generado exitosamente en 'data/dataset_transporte.csv'")