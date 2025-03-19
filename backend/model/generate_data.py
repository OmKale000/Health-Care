import pandas as pd
import numpy as np
import os

# Ensure dataset directory exists
os.makedirs("dataset", exist_ok=True)

# Number of samples
num_samples = 1000

# Generate synthetic dataset
data = {
    "Age": np.random.randint(20, 80, num_samples),
    "BMI": np.round(np.random.uniform(18.5, 35.0, num_samples), 1),
    "BloodPressure": np.random.randint(80, 160, num_samples),
    "Glucose": np.random.randint(70, 200, num_samples),
    "Cholesterol": np.random.randint(100, 300, num_samples),
}

# Function to determine disease risk
def determine_risk(bp, glucose, cholesterol, bmi):
    if bp > 140 or glucose > 180 or cholesterol > 250 or bmi > 30:
        return "High"
    elif bp > 120 or glucose > 140 or cholesterol > 200 or bmi > 25:
        return "Medium"
    else:
        return "Low"

# Function to determine possible diseases based on risk factors
def determine_diseases(bp, glucose, cholesterol, bmi):
    diseases = []
    if bp > 140:
        diseases.append("Hypertension")
    if glucose > 180:
        diseases.append("Diabetes")
    if cholesterol > 250:
        diseases.append("Heart Disease")
    if bmi > 30:
        diseases.append("Obesity")
    
    return ", ".join(diseases) if diseases else "No major risk detected"

# Function to determine precautionary measures
def determine_precautions(diseases):
    precautions = {
        "Hypertension": "Reduce salt intake, exercise regularly, avoid stress.",
        "Diabetes": "Maintain a low-sugar diet, exercise daily, monitor glucose levels.",
        "Heart Disease": "Avoid fatty foods, exercise regularly, control cholesterol levels.",
        "Obesity": "Follow a balanced diet, avoid junk food, engage in physical activity."
    }
    
    if diseases == "No major risk detected":
        return "Maintain a healthy lifestyle."
    
    return ", ".join([precautions[d] for d in diseases.split(", ") if d in precautions])

# Apply risk, disease prediction, and precautions
data["RiskLevel"] = [determine_risk(bp, glucose, chol, bmi) for bp, glucose, chol, bmi in zip(data["BloodPressure"], data["Glucose"], data["Cholesterol"], data["BMI"])]
data["ExpectedDiseases"] = [determine_diseases(bp, glucose, chol, bmi) for bp, glucose, chol, bmi in zip(data["BloodPressure"], data["Glucose"], data["Cholesterol"], data["BMI"])]
data["Precautions"] = [determine_precautions(disease) for disease in data["ExpectedDiseases"]]

# Convert to DataFrame
df = pd.DataFrame(data)

# Save dataset
df.to_csv("dataset/health_data.csv", index=False)
print("✅ Dataset successfully generated and saved as 'dataset/health_data.csv'.")
