import pandas as pd

def cargar_y_limpiar(path="data/Database.xlsx"):
    df = pd.read_excel(path)

    # Eliminar duplicados
    df = df.drop_duplicates()

    # Rellenar vacíos
    df = df.fillna(method="ffill").fillna(method="bfill")

    # Renombrar columnas si es necesario
    df.columns = [col.strip().replace(" ", "_") for col in df.columns]

    return df


if __name__ == "__main__":
    df = cargar_y_limpiar()
    df.to_csv("data/datos_limpios_mina.csv", index=False)
    print("Datos preparados y exportados.")

