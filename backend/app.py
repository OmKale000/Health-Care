from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from model.predict import predict_risk  # Ensure proper import

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    return "✅ Disease Risk Prediction API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        # Validate request data
        required_keys = ["Age", "BMI", "BloodPressure", "Glucose", "Cholesterol"]
        if not all(key in data for key in required_keys):
            return jsonify({"error": "Missing required input values"}), 400

        logging.info(f"📩 Received Data: {data}")

        # Extract user input (Gender Removed)
        age = data["Age"]
        bmi = data["BMI"]
        blood_pressure = data["BloodPressure"]
        glucose = data["Glucose"]
        cholesterol = data["Cholesterol"]

        # Call the prediction function without gender
        result = predict_risk({
            "Age": age,
            "BMI": bmi,
            "BloodPressure": blood_pressure,
            "Glucose": glucose,
            "Cholesterol": cholesterol
        })

        logging.info(f"📊 Prediction Output: {result}")
        return jsonify(result)

    except Exception as e:
        logging.error(f"❌ Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
