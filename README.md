# 📊 Customer Churn Prediction App

This project is a **Streamlit web application** that predicts whether a customer is likely to **churn** or **stay** based on input features like age, gender, contract type, and monthly charges. It uses a trained **XGBoost classifier**, with proper preprocessing (including encoding and scaling) applied.

---

## 🚀 Features

- Clean and interactive **Streamlit UI**
- Preprocessing includes:
  - One-hot encoding for categorical variables
  - Standard scaling for all features
- Uses an **XGBoost model** trained for 100% accuracy on a sample dataset
- Reusable prediction logic separated into a `predictor.py` module
- Live **real-time predictions** from user input

---

## 🧠 Model Info

- **Model**: XGBoost Classifier
- **Preprocessing**: `get_dummies()` + `StandardScaler`
- **Trained Features**:
  - `Age`
  - `Gender`
  - `Tenure`
  - `MonthlyCharges`
  - `ContractType`
  - `InternetService`
  - `TechSupport`

---

## 📦 Project Structure

Churn-Prediction/
├── artifacts/
│ ├── model.joblib # Trained XGBoost model
│ └── scaler.joblib # Scaler + column metadata
├── streamlit-app/
│ ├── app.py # Main Streamlit app
│ └── predictor.py # Prediction logic
├── requirements.txt
└── README.md
