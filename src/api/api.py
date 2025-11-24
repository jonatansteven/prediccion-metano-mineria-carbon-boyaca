from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(
    title="API de Predicción de Metano",
    description="Predicción del gas metano (COMB) en minería de carbón usando un modelo de regresión lineal.",
    version="1.0.0"
)

# Cargar modelo y scaler
model = joblib.load("modelo_final/modelo_regresion_metano.pkl")
scaler = joblib.load("modelo_final/scaler.pkl")
feature_names = joblib.load("modelo_final/feature_names.pkl")


class DatosEntrada(BaseModel):
    O2_min: float
    O2_max: float
    CO: float
    H2S: float
    Temp: float


@app.get("/")
def home():
    return {"mensaje": "API funcionando. Ve a /docs para probarla."}


@app.post("/predict")
def predict(data: DatosEntrada):

    O2_avg = (data.O2_min + data.O2_max) / 2

    # Ordenar datos según feature_names
    entrada = {
        "O2_min": data.O2_min,
        "O2_max": data.O2_max,
        "O2_avg": O2_avg,
        "CO": data.CO,
        "H2S": data.H2S,
        "Temp": data.Temp
    }

    X = np.array([[entrada[col] for col in feature_names]])

    X_scaled = scaler.transform(X)

    pred = model.predict(X_scaled)[0]

    return {
        "metano_predicho": float(round(pred, 4)),
        "unidad": "%",
        "nivel_riesgo": (
            "NORMAL" if pred < 0.5 else
            "PRECAUCIÓN" if pred < 1.0 else
            "PELIGRO" if pred < 1.5 else
            "EVACUAR"
        )
    }

