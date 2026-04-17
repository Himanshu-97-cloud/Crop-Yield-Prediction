import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import requests
from src.predict import predict, get_valid_options

# 🔹 ADD YOUR API KEY HERE
API_KEY = os.getenv("API_KEY")

st.title("🌾 Crop Yield Prediction")

# ───────── STEP 1: LOCATION INPUT ─────────
st.subheader("📍 Step 1: Enter Location")

state = st.text_input("Enter City / State (e.g., Ahmedabad)")
month = st.number_input("Month (1-12)", min_value=1, max_value=12, value=6)
year = st.number_input("Year", value=2020)

# ───────── WEATHER FUNCTION ─────────
def get_weather(city):
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    res = requests.get(url)

    if res.status_code != 200:
        raise Exception("❌ Invalid location or API error")

    data = res.json()

    temp = data["current"]["temp_c"]
    rainfall = data["current"]["precip_mm"]
    humidity = data["current"]["humidity"]

    return temp, rainfall, humidity

# ───────── SEASON FUNCTION ─────────
def get_season(month):
    if 6 <= month <= 10:
        return "Kharif"
    elif month <= 3 or month >= 11:
        return "Rabi"
    else:
        return "Zaid"

# ───────── FETCH WEATHER ─────────
if st.button("Fetch Details"):
    try:
        temp, rain, humidity = get_weather(state)
        season = get_season(month)

        # Save in session
        st.session_state["weather"] = {
            "temp": temp,
            "rain": rain,
            "humidity": humidity,
            "season": season
        }

        st.success("✅ Weather fetched successfully")

        st.info(f"""
        🌡️ Temperature: {temp} °C  
        🌧️ Rainfall: {rain} mm  
        💧 Humidity: {humidity}%  
        🌱 Season: {season}
        """)

    except Exception as e:
        st.error(str(e))

# ───────── STEP 2: USER INPUTS ─────────
if "weather" in st.session_state:

    st.subheader("🌱 Step 2: Enter Crop Details")

    areas, crops = get_valid_options()

    crop = st.selectbox("Select Crop", crops)
    area = st.number_input("Area (hectare)", min_value=1.0, value=100.0)
    fertilizer = st.number_input("Fertilizer (tonnes)", min_value=0.0, value=50.0)

    # ───────── PREDICT ─────────
    if st.button("Predict Yield"):
        try:
            w = st.session_state["weather"]

            result = predict(
                area=areas[0],   # using trained area
                crop=crop,
                year=year,
                rain=w["rain"],
                pest=fertilizer,
                temp=w["temp"]
            )

            st.success(f"🌾 Predicted Yield: {round(result,2)} hg/ha")

            # Show R² score
            if os.path.exists("models/r2.txt"):
                with open("models/r2.txt") as f:
                    r2 = float(f.read())
                    st.write(f"📊 Model Accuracy (R²): {round(r2,4)}")

        except Exception as e:
            st.error(str(e))

# ───────── GRAPHS SECTION ─────────
st.subheader("📊 Insights")

# Crop vs Yield
if os.path.exists("outputs/crop_vs_yield.png"):
    st.markdown("### 🌱 Crop vs Yield")
    st.image("outputs/crop_vs_yield.png", use_container_width=True)

# Yield Distribution
if os.path.exists("outputs/yield_distribution.png"):
    st.markdown("### 📈 Yield Distribution")
    st.image("outputs/yield_distribution.png", use_container_width=True)

# Correlation Heatmap
if os.path.exists("outputs/correlation_heatmap.png"):
    st.markdown("### 🔥 Correlation Heatmap")
    st.image("outputs/correlation_heatmap.png", use_container_width=True)