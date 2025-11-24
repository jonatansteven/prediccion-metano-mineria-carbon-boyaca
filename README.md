# Predicción de Metano (CH₄) en Minería de Carbón - Boyacá

**Universidad ECCI - 2025**  
**Integrantes:** Jonatan Gómez • Nicolás González • Nicolás Palomino

## Objetivo
Desarrollar un modelo de **regresión lineal** para predecir niveles de metano combustible (COMB) en tiempo real usando sensores ambientales.

### Resultados del Modelo
- R²: **~0.85 - 0.95** (dependiendo del dataset)
- RMSE: **< 0.15%**
- MAE: **< 0.12%**

## Estructura del Repositorio
├── modelo_completo.py          ← Script completo (limpieza + entrenamiento + gráficos)
├── datos_limpios_mina.csv      ← Datos procesados listos para usar
├── modelo_final/               ← Modelo entrenado (.pkl)
├── requirements.txt            ← Dependencias
└── README.md                   ← Este archivo
