from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI(
    title="API de Predicción de Metano",
    description="Modelo predictivo de metano (COMB) para minería de carbón",
    version="1.0"
)

# Cargar modelo
model = joblib.load("modelo_final/modelo_regresion_metano.pkl")

# Cargar escalador
scaler = joblib.load("modelo_final/scaler.pkl")

# Cargar nombres de columnas
feature_names = joblib.load("modelo_final/feature_names.pkl")


@app.get("/")
def home():
    return {"mensaje": "API funcionando correctamente. Usa /predict para hacer predicciones."}


@app.get("/predict")
def predict(O2_min: float, O2_max: float, CO: float, H2S: float, Temp: float):

    O2_avg = (O2_min + O2_max) / 2

    datos = np.array([[O2_min, O2_max, O2_avg, CO, H2S, Temp]])

    datos_scaled = scaler.transform(datos)

    pred = model.predict(datos_scaled)[0]

    return {
        "metano_predicho": float(round(pred, 4)),
        "unidad": "%",
        "estado": (
            "NORMAL" if pred < 0.5 else
            "PRECAUCIÓN" if pred < 1.0 else
            "RIESGO" if pred < 1.5 else
            "EVACUACIÓN"
        )
    }
