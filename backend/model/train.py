import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
df = pd.read_csv("dataset/health_data.csv")

# Debugging: Print column names to verify
print("Dataset Columns:", df.columns)

# Ensure column names match exactly (Gender Removed)
expected_columns = ["Age", "BMI", "BloodPressure", "Glucose", "Cholesterol", "RiskLevel"]
missing_columns = [col for col in expected_columns if col not in df.columns]
if missing_columns:
    raise ValueError(f"Missing columns in dataset: {missing_columns}")

# Check for missing values
if df.isnull().sum().sum() > 0:
    print("Warning: Dataset contains missing values. Consider cleaning the data.")

# Define features (X) and target (y) - Gender Removed
X = df[["Age", "BMI", "BloodPressure", "Glucose", "Cholesterol"]]
y = df["RiskLevel"].map({"Low": 0, "Medium": 1, "High": 2})  # Convert risk levels to numeric

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing pipeline
scaler = StandardScaler()
model = RandomForestClassifier(n_estimators=100, random_state=42)

pipeline = Pipeline([
    ("scaler", scaler),
    ("classifier", model)
])

# Train the model
pipeline.fit(X_train, y_train)

# Model evaluation
y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Save the trained model and scaler
joblib.dump(pipeline, "model/disease_risk_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")

# Display accuracy
print("✅ Model trained and saved successfully.")
print(f"🎯 Model Accuracy: {accuracy * 100:.2f}%")
