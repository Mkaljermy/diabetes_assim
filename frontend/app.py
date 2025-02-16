import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import base64

API_URL = "http://localhost:8000/predict"

# Set page config
st.set_page_config(page_title="Diabetes Prediction App", page_icon="🩸", layout="centered")

# Custom styling
st.markdown(
    """
    <style>
    body {
        background-color: #f7f7f7;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 1px solid #ccc;
    }
    .stNumberInput>div>div>input {
        border-radius: 10px;
        border: 1px solid #ccc;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #ff1c1c;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header with image
st.title("🩸 Diabetes Prediction App")
st.markdown("Enter your details below to predict your risk of diabetes.")

# Input fields
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", min_value=0.0, max_value=13.0, value=0.0, step=0.1, format="%.1f")
    glucose = st.number_input("Glucose", min_value=44.0, max_value=199.0, value=100.0, step=0.1, format="%.1f")
    blood_pressure = st.number_input("Blood Pressure", min_value=38.0, max_value=106.0, value=70.0, step=0.1, format="%.1f")
    skin_thickness = st.number_input("Skin Thickness", min_value=0.0, max_value=63.0, value=20.0, step=0.1, format="%.1f")

with col2:
    insulin = st.number_input("Insulin", min_value=0.0, max_value=318.0, value=80.0, step=1.0, format="%.1f")
    bmi = st.number_input("BMI", min_value=18.2, max_value=49.7, value=25.0, step=0.01, format="%.2f")
    diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0780, max_value=1.1910, value=0.5, step=0.0001, format="%.4f")
    age = st.number_input("Age", min_value=21, max_value=66, value=30, step=1)

# Prediction button
if st.button("🔍 Predict"):
    input_data = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": diabetes_pedigree,
        "Age": age
    }
    
    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            prediction = result['prediction']
            probability = result.get('probability', 0) * 100
            
            if prediction:
                st.error(f"⚠️ Prediction: Diabetic (Risk: {probability:.2f}%)")
                st.image("D:\diabetes_assim\\frontend\\risk.png", width=150)
            else:
                st.success(f"✅ Prediction: Not Diabetic (Risk: {probability:.2f}%)")
                st.image("D:\diabetes_assim\\frontend\happy.png", width=150)
        else:
            st.error(f"Error: {response.status_code}")
    except Exception as e:
        st.error(f"Exception: {str(e)}")