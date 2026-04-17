import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# load dataset
df = pd.read_csv("dataset/yield_df.csv")

# remove unwanted columns
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

os.makedirs("outputs", exist_ok=True)

# 🔹 1. Yield Distribution
plt.figure(figsize=(8,5))
plt.hist(df["hg/ha_yield"], bins=50)
plt.title("Yield Distribution")
plt.xlabel("Yield (hg/ha)")
plt.ylabel("Count")
plt.savefig("outputs/yield_distribution.png")
plt.close()

# 🔹 2. Crop vs Yield
top_crops = df.groupby("Item")["hg/ha_yield"].mean().sort_values().tail(15)

plt.figure(figsize=(10,6))
top_crops.plot(kind="barh")
plt.title("Top Crops by Yield")
plt.xlabel("Yield")
plt.savefig("outputs/crop_vs_yield.png")
plt.close()

# 🔹 3. Correlation Heatmap
num_cols = [
    "Year",
    "average_rain_fall_mm_per_year",
    "pesticides_tonnes",
    "avg_temp",
    "hg/ha_yield"
]

plt.figure(figsize=(8,6))
sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("outputs/correlation_heatmap.png")
plt.close()

print("EDA graphs generated successfully")