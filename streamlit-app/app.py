import streamlit as st
from predictor import predict

st.set_page_config(page_title="Churn Prediction App", layout="centered")

st.markdown("""
    <h1 style="text-align:center; color:#4CAF50;">📊 Customer Churn Prediction</h1>
    <p style="text-align:center;">Fill out the details below to check if a customer is likely to churn.</p>
""", unsafe_allow_html=True)

# --- UI Inputs in Columns ---
col1, col2 = st.columns(2)

with col1:
    Age = st.number_input("🧓 Age", min_value=18, max_value=100, step=1)
    Tenure = st.number_input("⏳ Tenure (in months)", min_value=0, max_value=100, step=1)
    MonthlyCharges = st.number_input("💸 Monthly Charges", min_value=0.0, step=0.1)

with col2:
    Gender = st.selectbox("🚻 Gender", ['Male', 'Female'])
    ContractType = st.selectbox("📄 Contract Type", ['Month-to-month', 'One year', 'Two year'])
    InternetService = st.selectbox("🌐 Internet Service", ['DSL', 'Fiber optic', 'No'])
    TechSupport = st.selectbox("🛠️ Tech Support", ['Yes', 'No'])

# --- Assemble input dict ---
input_dict = {
    'Age': Age,
    'Gender': Gender,
    'Tenure': Tenure,
    'MonthlyCharges': MonthlyCharges,
    'ContractType': ContractType,
    'InternetService': InternetService,
    'TechSupport': TechSupport
}

# --- Predict ---
if st.button("🔍 Predict"):
    prediction = predict(input_dict)
    
    st.markdown("---")
    st.subheader("🔎 Prediction Result")
    
    if prediction[0] == 1:
        st.error("⚠️ The customer is likely to **CHURN**.")
    else:
        st.success("✅ The customer is likely to **STAY**.")

st.markdown("""
    <hr style="margin-top: 30px;">
    <div style="text-align: center; color: gray;">
       Powered by Streamlit & XGBoost
    </div>
""", unsafe_allow_html=True)
