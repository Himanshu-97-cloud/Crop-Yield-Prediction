# 🌾 Crop Yield Prediction (Machine Learning Project)

## 📌 Overview

This project predicts crop yield (hg/ha) using Machine Learning based on environmental and agricultural inputs such as rainfall, temperature, crop type, and pesticide usage.

It includes a complete end-to-end ML pipeline:

* Data preprocessing
* Model training
* Prediction system
* Streamlit web application
* Exploratory Data Analysis (EDA)

---

## 🚀 Features

* End-to-end ML pipeline (Preprocessing → Training → Prediction)
* Random Forest Regressor model
* Interactive Streamlit web application
* Weather API integration
* Data visualization using EDA

---

## 🛠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn
* Streamlit

---

## 📁 Project Structure

```
crop-yield-prediction/
│
├── app/            # Streamlit application
├── src/            # ML pipeline (preprocess, train, predict)
├── notebooks/      # EDA scripts
├── dataset/        # dataset (see dataset/README.md)
├── models/         # trained models (see models/README.md)
├── outputs/        # generated graphs (see outputs/README.md)
│
├── README.md
├── requirements.txt
```

---

## ⚙️ Setup Instructions

Follow these steps to run the project locally:

---

### 🔹 Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 Step 2: Download Dataset

Download dataset from Kaggle:
https://www.kaggle.com/datasets/patelris/crop-yield-prediction-dataset

After downloading:

* Extract the dataset
* Place the file inside the `dataset/` folder

Required file:

```
dataset/yield_df.csv
```

---

### 🔹 Step 3: Generate Model Files

Run the following:

```bash
python src/preprocess.py
python src/train.py
```

This will:

* preprocess the dataset
* train the model
* create required files in `models/` folder

---

### 🔹 Step 4: Generate EDA Graphs

```bash
python notebooks/eda.py
```

This will generate visualization images inside `outputs/`

---

### 🔹 Step 5: Setup API Key

This project uses Weather API.

1. Go to: https://www.weatherapi.com/
2. Sign up and get your free API key

Create a `.env` file in the root folder and add:

```
API_KEY=your_api_key_here
```

---

### 🔹 Step 6: Run the Application

```bash
streamlit run app/app.py
```

---

## 📊 Output

* Crop yield prediction (hg/ha)
* Weather-based input integration
* Data visualization graphs

---

## ⚠️ Important Notes

* `dataset/`, `models/`, and `outputs/` folders are intentionally empty
* Follow setup steps to generate required files
* `.env` file is not included for security reasons

---

## 👨‍💻 Author

Himanshu Pal
