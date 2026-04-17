import pandas as pd
import pickle
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("dataset/processed_data.csv")
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

X = df.drop("hg/ha_yield", axis=1)
y = df["hg/ha_yield"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

pred = model.predict(X_test)

r2 = r2_score(y_test, pred)
rmse = np.sqrt(mean_squared_error(y_test, pred))

print("R2:", r2)
print("RMSE:", rmse)

os.makedirs("models", exist_ok=True)
pickle.dump(model, open("models/best_model.pkl", "wb"))

# Save R2 for UI
with open("models/r2.txt", "w") as f:
    f.write(str(r2))