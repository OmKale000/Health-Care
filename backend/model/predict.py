import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load("model/disease_risk_model.pkl")
scaler = joblib.load("model/scaler.pkl")

# Disease and precaution mapping
disease_mapping = {
    "Normal Blood Pressure": "Maintain a healthy lifestyle with balanced diet and exercise.",
    "Elevated Blood Pressure": "Monitor your BP, reduce salt intake, and exercise regularly.",
    "Hypertension Stage 1": "Consult a doctor, avoid processed foods, and manage stress.",
    "Hypertension Stage 2": "Requires medical supervision, reduce sodium intake, and take prescribed medication.",
    "Hypertensive Crisis": "Seek emergency care immediately!",
    "Hypotension": "Stay hydrated, consume more salt, and avoid prolonged standing.",
    
    "Normal Blood Sugar": "Maintain a balanced diet and regular physical activity.",
    "Pre-Diabetes": "Exercise regularly and control sugar intake to prevent diabetes.",
    "Diabetes": "Follow a low-sugar diet, take prescribed medication, and monitor glucose levels.",
    "Severe Diabetes": "Strict medical supervision is needed. Regular checkups and medication are essential.",
    "Hypoglycemia": "Consume small, frequent meals with complex carbohydrates. Avoid excessive sugar intake.",
    
    "Normal Cholesterol": "Keep a balanced diet and stay active.",
    "Borderline High Cholesterol": "Reduce fatty foods and exercise regularly.",
    "High Cholesterol": "Consult a doctor, limit saturated fats, and include more fiber in your diet.",
    "Very High Cholesterol": "Strict diet and medication may be required. Seek medical advice.",
    
    "Heart Disease": "Control cholesterol levels, avoid fatty foods, and exercise regularly.",
    "Obesity": "Follow a balanced diet, avoid junk food, and engage in physical activity.",
    "Severe Obesity": "Medical supervision is advised for weight management.",
    "Underweight": "Increase calorie intake with healthy fats and proteins, and consider strength training.",
    "Anemia": "Consume iron-rich foods like leafy greens, red meat, and vitamin C-rich foods."
}

# Function to determine possible diseases
def determine_diseases(bp, glucose, cholesterol, bmi):
    diseases = []
    
    # Blood Pressure Classification
    if bp < 90:
        diseases.append("Hypotension")
    elif 90 <= bp < 120:
        diseases.append("Normal Blood Pressure")
    elif 120 <= bp < 130:
        diseases.append("Elevated Blood Pressure")
    elif 130 <= bp < 140:
        diseases.append("Hypertension Stage 1")
    elif 140 <= bp < 180:
        diseases.append("Hypertension Stage 2")
    else:
        diseases.append("Hypertensive Crisis")
    
    # Blood Sugar Classification
    if glucose < 70:
        diseases.append("Hypoglycemia")
    elif 70 <= glucose < 100:
        diseases.append("Normal Blood Sugar")
    elif 100 <= glucose < 126:
        diseases.append("Pre-Diabetes")
    elif 126 <= glucose < 200:
        diseases.append("Diabetes")
    else:
        diseases.append("Severe Diabetes")
    
    # Cholesterol Classification
    if cholesterol < 200:
        diseases.append("Normal Cholesterol")
    elif 200 <= cholesterol < 239:
        diseases.append("Borderline High Cholesterol")
    elif 240 <= cholesterol < 280:
        diseases.append("High Cholesterol")
    else:
        diseases.append("Very High Cholesterol")
    
    # BMI Classification
    if bmi < 18.5:
        diseases.append("Underweight")
    elif 18.5 <= bmi < 25:
        diseases.append("Normal BMI")
    elif 25 <= bmi < 30:
        diseases.append("Overweight")
    elif 30 <= bmi < 35:
        diseases.append("Obesity")
    else:
        diseases.append("Severe Obesity")
    
    # Anemia Check (Low BMI + Low BP)
    if bmi < 18.5 and bp < 90:
        diseases.append("Anemia")

    return diseases if diseases else ["No major risk detected"]

# Function to determine precautionary measures
def determine_precautions(diseases):
    return [disease_mapping[d] for d in diseases if d in disease_mapping] or ["Maintain a healthy lifestyle."]

# Function to predict risk level and additional information
def predict_risk(data):
    try:
        # Debugging: Print received data
        print("📩 Received Data:", data)

        # Extract features from request
        age = data.get("Age")
        bmi = data.get("BMI")
        blood_pressure = data.get("BloodPressure")
        glucose = data.get("Glucose")
        cholesterol = data.get("Cholesterol")

        # Validate input
        if None in [age, bmi, blood_pressure, glucose, cholesterol]:
            raise ValueError("Missing required input values")

        # Prepare input data
        features = np.array([[age, bmi, blood_pressure, glucose, cholesterol]])

        # Standardize input features
        features = scaler.transform(features)

        # Predict risk level
        prediction = model.predict(features)
        risk_levels = {0: "Low", 1: "Medium", 2: "High"}
        risk_level = risk_levels.get(int(prediction[0]), "Unknown")

        # Get expected diseases and precautions
        diseases = determine_diseases(blood_pressure, glucose, cholesterol, bmi)
        precautions = determine_precautions(diseases)

        return {
            "risk_level": risk_level,
            "expected_diseases": diseases,
            "precautionary_measures": precautions
        }
    
    except Exception as e:
        print(f"❌ Error: {e}")
        return {"error": str(e)}
