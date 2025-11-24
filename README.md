**Predicción de Metano (CH₄) en Minería de Carbón — Boyacá**
Universidad ECCI — Ingeniería · 2025

Autores: Jonatan Steven Gómez · Nicolás González · Nicolás Palomino

📌 Descripción del Proyecto

Este proyecto implementa un sistema completo de predicción del gas metano (COMB) en minas de carbón bajo tierra, utilizando:

Dispositivo Multidetector (O₂ mínimo, O₂ máximo, CO, H₂S y temperatura)

Limpieza y transformación de datos

Entrenamiento de un modelo de Regresión Lineal

Exportación del modelo

Creación de una API FastAPI para predicciones en tiempo real

Estructura profesional del repositorio

El objetivo es aportar a la seguridad minera mediante detección temprana de riesgos explosivos.

Tecnologías Utilizadas

| Categoría           | Tecnologías                 |
| ------------------- | --------------------------- |
| Lenguaje            | Python 3                    |
| Data Science        | Pandas, NumPy, Scikit-learn |
| API                 | FastAPI, Uvicorn            |
| Guardado de modelos | Joblib                      |
| Visualización       | Matplotlib                  |
| Otros               | OpenPyXL                    |

prediccion-metano-mineria-carbon-boyaca/
│
├── src/
│   ├── api/
│   │   └── api.py                   # API de predicción
│   ├── model/
│   │   └── entrenar_modelo.py       # Entrenamiento del modelo
│   └── data_preparation/
│       └── preparar_datos.py        # Limpieza de datos
│
├── modelo_final/
│   ├── modelo_regresion_metano.pkl
│   ├── scaler.pkl
│   ├── feature_names.pkl
│   ├── coeficientes.csv
│   └── metrics.txt
│
├── data/
│   ├── Database.xlsx
│   └── datos_limpios_mina.csv
│
├── notebooks/
│   └── Modelo_de_Prediccion.ipynb
│
├── README.md
├── requirements.txt
└── .gitignore

Cómo ejecutar el proyecto
Instalar dependencias
pip install -r requirements.txt

Entrenar el modelo desde cero

Ejecutar el script:

python src/model/entrenar_modelo.py


Esto generará:

modelo_regresion_metano.pkl

scaler.pkl

feature_names.pkl

coeficientes.csv

metrics.txt

API de Predicción (FastAPI)
Cómo iniciar la API

Ejecuta:

uvicorn src.api.api:app --reload

Endpoints
GET /

Prueba de vida
Devuelve un mensaje indicando que la API funciona.

POST /predict

Recibe datos ambientales y retorna el nivel predicho de metano.

Resultados del Modelo con 500 datos
Métrica	Resultado
R²	0.71
MAE	< 0.23%
RMSE	< 0.35%

El modelo presenta la capacidad de predicción para aplicaciones mineras.

Automatizar el entrenamiento con GitHub Actions

📬 Contacto

Creador: Jonatan Steven Gómez Avellaneda
Proyecto académico · Universidad ECCI
