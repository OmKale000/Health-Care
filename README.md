# AI-Powered Early Disease Risk Predictor

## 📌 Project Overview
The **AI-Powered Early Disease Risk Predictor** is a web-based application that evaluates an individual's health risk based on key health indicators such as **BMI, blood pressure, glucose levels, and cholesterol levels**. Using a machine learning model, it categorizes risk levels into **Low, Medium, or High** while also predicting possible diseases and providing precautionary measures.

---

## ✨ Key Features
- 📊 **Risk Level Prediction:** Categorizes health risk as **Low, Medium, or High**.
- 🏥 **Disease Prediction:** Identifies potential diseases such as **Diabetes, Hypertension, Heart Disease, Obesity, and Anemia**.
- 🔍 **Stage-Wise Classification:** Provides detailed health condition categories (e.g., **Pre-Diabetes, Hypertension Stage 1 & 2**).
- 💡 **Precautionary Measures:** Offers lifestyle and medical recommendations based on detected conditions.
- ⚡ **Machine Learning-Powered:** Utilizes a trained ML model for accurate predictions.
- 📱 **User-Friendly Web Interface:** Easy-to-use web UI for health risk assessment.

---

## 🚀 Technologies Used
### Backend:
- **Python** (Flask for API development)
- **Scikit-learn** (Machine Learning model)
- **Joblib** (Model storage and loading)
- **NumPy & Pandas** (Data processing)
- **OpenCV & TensorFlow** *(Future integration planned for AI-driven analysis)*

### Frontend:
- **React.js** (UI Development)
- **Tailwind CSS** (Styling)

### Database:
- **SQLite / Firebase (Future integration planned)**

---

## 🛠 Installation & Setup
### Prerequisites:
- **Python 3.8+**
- **Node.js & npm** (for frontend)
- **Virtual Environment (optional but recommended)**

### 🔹 Backend Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/ai-disease-risk-predictor.git
   cd ai-disease-risk-predictor
   ```
2. **Create a virtual environment:** *(Optional but recommended)*
   ```bash
   python -m venv venv
   source venv/bin/activate   # MacOS/Linux
   venv\Scripts\activate      # Windows
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Flask API:**
   ```bash
   python app.py
   ```
   API should now be running at `http://127.0.0.1:5000/`

### 🔹 Frontend Setup
1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```
2. **Install dependencies:**
   ```bash
   npm install
   ```
3. **Start the React development server:**
   ```bash
   npm start
   ```
   The web app should now be running at `http://localhost:3000/`

---

## 🔗 API Endpoints
### 1️⃣ **Health Risk Prediction**
- **Endpoint:** `/predict`
- **Method:** `POST`
- **Request Body (JSON):**
  ```json
  {
      "Age": 40,
      "BMI": 32,
      "BloodPressure": 145,
      "Glucose": 135,
      "Cholesterol": 260
  }
  ```
- **Response (JSON):**
  ```json
  {
      "risk_level": "High",
      "expected_diseases": [
          "Hypertension Stage 2",
          "Diabetes",
          "High Cholesterol",
          "Obesity"
      ],
      "precautionary_measures": [
          "Requires medical supervision, reduce sodium intake, and take prescribed medication.",
          "Follow a low-sugar diet, take prescribed medication, and monitor glucose levels.",
          "Consult a doctor, limit saturated fats, and include more fiber in your diet.",
          "Follow a balanced diet, avoid junk food, and engage in physical activity."
      ]
  }
  ```

---

## 📊 Machine Learning Model Details
- **Algorithm Used:** Logistic Regression / Random Forest *(Can be improved with Deep Learning in future versions)*
- **Training Data:** Publicly available health datasets with clinical readings
- **Features Considered:**
  - **Age**
  - **BMI (Body Mass Index)**
  - **Blood Pressure**
  - **Glucose Levels**
  - **Cholesterol Levels**

---

## 🎯 Future Improvements
- **📡 Integration with IoT devices** (e.g., wearables, smart health monitors)
- **🤖 AI-powered personalized health assistant**
- **📱 Mobile App Version**
- **🩺 Integration with real-time patient monitoring systems**

---

## 📝 Contributing
Interested in contributing? Follow these steps:
1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature-name`
3. **Commit changes:** `git commit -m "Added new feature"`
4. **Push to GitHub:** `git push origin feature-name`
5. **Submit a pull request** 🎉

---

## 👨‍💻 Team Members & Contact
-**Om Kale** - Developer

📧 **Contact:** ok176471@gmail.com

---

## 📜 License
This project is licensed under the **MIT License**. Feel free to modify and use it for your own research and applications.

