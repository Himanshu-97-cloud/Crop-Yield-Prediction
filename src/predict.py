import pickle
import pandas as pd

model = pickle.load(open("models/best_model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))
encoders = pickle.load(open("models/label_encoders.pkl", "rb"))

def predict(area, crop, year, rain, pest, temp):
    df = pd.DataFrame([{
        "Area": encoders["Area"].transform([area])[0],
        "Item": encoders["Item"].transform([crop])[0],
        "Year": year,
        "average_rain_fall_mm_per_year": rain,
        "pesticides_tonnes": pest,
        "avg_temp": temp
    }])

    df_scaled = scaler.transform(df)
    df_scaled = pd.DataFrame(df_scaled, columns=df.columns)
    return model.predict(df_scaled)[0]

def get_valid_options():
    return list(encoders["Area"].classes_), list(encoders["Item"].classes_)