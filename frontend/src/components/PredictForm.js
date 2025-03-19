import React, { useState } from "react";
import axios from "axios";

function PredictForm() {
    const [formData, setFormData] = useState({
        age: "",
        bmi: "",
        blood_pressure: "",
        glucose: "",
        cholesterol: ""
    });

    const [prediction, setPrediction] = useState(null);
    const [expectedDiseases, setExpectedDiseases] = useState([]);
    const [precautions, setPrecautions] = useState([]);
    const [error, setError] = useState(null);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const transformedData = {
            Age: Number(formData.age),
            BMI: Number(formData.bmi),
            BloodPressure: Number(formData.blood_pressure),
            Glucose: Number(formData.glucose),
            Cholesterol: Number(formData.cholesterol)
        };

        try {
            const response = await axios.post("http://127.0.0.1:5000/predict", transformedData);

            setPrediction(response.data.risk_level);
            setExpectedDiseases(response.data.expected_diseases || []);
            setPrecautions(response.data.precautionary_measures || []);
            setError(null);
        } catch (error) {
            console.error("Error fetching prediction:", error);
            setError("Failed to get prediction. Please try again.");
        }
    };

    return (
        <div style={styles.container}>
            <h2 style={styles.heading}>Enter Health Data</h2>
            <form onSubmit={handleSubmit} style={styles.form}>
                <input type="number" name="age" placeholder="Age" value={formData.age} onChange={handleChange} required style={styles.input} />
                <input type="number" name="bmi" placeholder="BMI" value={formData.bmi} onChange={handleChange} required style={styles.input} />
                <input type="number" name="blood_pressure" placeholder="Blood Pressure" value={formData.blood_pressure} onChange={handleChange} required style={styles.input} />
                <input type="number" name="glucose" placeholder="Glucose" value={formData.glucose} onChange={handleChange} required style={styles.input} />
                <input type="number" name="cholesterol" placeholder="Cholesterol" value={formData.cholesterol} onChange={handleChange} required style={styles.input} />

                <button type="submit" style={styles.button}>Predict</button>
            </form>

            {prediction !== null && (
                <div style={styles.resultContainer}>
                    <h3 style={styles.result}>Predicted Risk Level: {prediction}</h3>
                    
                    {expectedDiseases.length > 0 && (
                        <div style={styles.listContainer}>
                            <h4>Possible Diseases:</h4>
                            <ul>
                                {expectedDiseases.map((disease, index) => (
                                    <li key={index}>{disease}</li>
                                ))}
                            </ul>
                        </div>
                    )}

                    {precautions.length > 0 && (
                        <div style={styles.listContainer}>
                            <h4>Precautionary Measures:</h4>
                            <ul>
                                {precautions.map((precaution, index) => (
                                    <li key={index}>{precaution}</li>
                                ))}
                            </ul>
                        </div>
                    )}
                </div>
            )}

            {error && <p style={styles.error}>{error}</p>}
        </div>
    );
}

const styles = {
    container: { textAlign: "center", maxWidth: "400px", margin: "auto", padding: "20px", border: "1px solid #ddd", borderRadius: "8px", boxShadow: "2px 2px 10px rgba(0,0,0,0.1)" },
    heading: { color: "#333" },
    form: { display: "flex", flexDirection: "column", gap: "10px" },
    input: { padding: "10px", borderRadius: "5px", border: "1px solid #ccc", fontSize: "16px" },
    button: { padding: "10px", border: "none", borderRadius: "5px", backgroundColor: "#28a745", color: "#fff", fontSize: "16px", cursor: "pointer" },
    resultContainer: { marginTop: "20px", textAlign: "left" },
    result: { color: "#007bff", fontSize: "18px", fontWeight: "bold" },
    listContainer: { marginTop: "10px", background: "#f9f9f9", padding: "10px", borderRadius: "5px" },
    error: { color: "red", fontSize: "14px" }
};

export default PredictForm;
