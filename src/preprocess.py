import pandas as pd
import pickle
import os
from sklearn.preprocessing import LabelEncoder, StandardScaler

df = pd.read_csv("dataset/yield_df.csv")
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
df = df.dropna()

encoders = {}
for col in ["Area", "Item"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

X = df.drop("hg/ha_yield", axis=1)
y = df["hg/ha_yield"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

os.makedirs("models", exist_ok=True)
pickle.dump(encoders, open("models/label_encoders.pkl", "wb"))
pickle.dump(scaler, open("models/scaler.pkl", "wb"))

df_scaled = pd.DataFrame(X_scaled, columns=X.columns)
df_scaled["hg/ha_yield"] = y
df_scaled.to_csv("dataset/processed_data.csv", index=False)