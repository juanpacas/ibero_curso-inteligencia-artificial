import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

def entrenar_modelo():
    # 1. Cargar datos
    df = pd.read_csv('data/dataset_transporte.csv')
    
    # 2. Preprocesamiento (Convertir variables categóricas a numéricas)
    df_encoded = pd.get_dummies(df, columns=['Dia_Semana', 'Clima'], drop_first=True)
    
    X = df_encoded.drop('Nivel_Retraso', axis=1)
    y = df_encoded['Nivel_Retraso']
    
    # 3. División Entrenamento / Prueba (80% / 20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # 4. Entrenamiento del Árbol de Decisión
    inicio = time.perf_counter()
    clf = DecisionTreeClassifier(max_depth=4, criterion='entropy', random_state=42)
    clf.fit(X_train, y_train)
    fin = time.perf_counter()
    
    # 5. Evaluación
    y_pred = clf.predict(X_test)
    exactitud = accuracy_score(y_test, y_pred)
    
    print("\n==================================================")
    print(" MODELO DE APRENDIZAJE SUPERVISADO (ÁRBOL DE DECISIÓN)")
    print("==================================================")
    print(f" Tiempo de entrenamiento: {(fin - inicio)*1000:.4f} ms")
    print(f" Exactitud del modelo (Accuracy): {exactitud * 100:.2f}%\n")
    
    print("--- REPORTE DE CLASIFICACIÓN ---")
    print(classification_report(y_test, y_pred))
    
    # 6. Extracción de Reglas de Decisión (Capítulo 17)
    print("--- REGLAS EXTRAÍDAS DEL ÁRBOL ---")
    reglas = export_text(clf, feature_names=list(X.columns))
    print(reglas)

if __name__ == "__main__":
    entrenar_modelo()