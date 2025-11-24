import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import joblib

# Cargar datos
df = pd.read_csv("data/datos_limpios_mina.csv")

# Crear O2 promedio
df["O2_avg"] = (df["O2_min"] + df["O2_max"]) / 2

# Variables
features = ["O2_min", "O2_max", "O2_avg", "CO", "H2S", "Temp"]
target = "COMB"

X = df[features]
y = df[target]

# Escalar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Entrenar modelo
model = LinearRegression()
model.fit(X_scaled, y)

# Guardar artefactos
joblib.dump(model, "modelo_final/modelo_regresion_metano.pkl")
joblib.dump(scaler, "modelo_final/scaler.pkl")
joblib.dump(features, "modelo_final/feature_names.pkl")

# Guardar coeficientes
coef_df = pd.DataFrame({
    "feature": features,
    "coeficiente": model.coef_
})
coef_df.to_csv("modelo_final/coeficientes.csv", index=False)

with open("modelo_final/metrics.txt", "w") as f:
    f.write(f"Intercept: {model.intercept_}\n")
    f.write("Modelo entrenado correctamente.\n")

