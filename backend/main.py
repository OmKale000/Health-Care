from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model
model = joblib.load("model/disease_risk_model.pkl")

# Initialize FastAPI app
app = FastAPI()

# Define request data model (Gender Removed)
class HealthData(BaseModel):
    Age: int
    BMI: float
    BloodPressure: float
    Glucose: float
    Cholesterol: float

@app.post("/predict/")
def predict_risk(data: HealthData):
    try:
        # Convert input data to model-compatible format
        features = np.array([[data.Age, data.BMI, data.BloodPressure, data.Glucose, data.Cholesterol]])

        # Predict risk level
        prediction = model.predict(features)
        return {"risk_level": int(prediction[0])}
    except Exception as e:
        return {"error": str(e)}
