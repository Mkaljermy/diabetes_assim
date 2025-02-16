from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

# Load model and scaler separately
model = joblib.load('D:\diabetes_assim\model\diabetes_model.pkl')  # Use double backslashes for Windows paths
scaler = joblib.load('D:\diabetes_assim\model\scaler.pkl')  # Load the scaler

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class DiabetesData(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float

@app.post("/predict")
def predict(data: DiabetesData):
    # Convert input data to numpy array
    input_data = np.array([[
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age
    ]])

    # Extract columns to scale
    columns_to_scale = ['Insulin', 'SkinThickness', 'BloodPressure', 'Glucose']
    input_data_to_scale = np.array([
        [data.Insulin, data.SkinThickness, data.BloodPressure, data.Glucose]
    ])

    # Scale the specified columns
    scaled_columns = scaler.transform(input_data_to_scale)

    # Replace the original columns with scaled values
    input_data[0, 4] = scaled_columns[0, 0]  # Insulin
    input_data[0, 3] = scaled_columns[0, 1]  # SkinThickness
    input_data[0, 2] = scaled_columns[0, 2]  # BloodPressure
    input_data[0, 1] = scaled_columns[0, 3]  # Glucose

    # Predict
    prediction = model.predict(input_data)[0]  # Use input_data instead of scaled_input
    probability = model.predict_proba(input_data)[0][1]  # Use input_data instead of scaled_input

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }