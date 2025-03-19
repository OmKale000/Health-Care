import pandas as pd
import numpy as np

# Load original dataset
df = pd.read_csv("dataset/health_data.csv")

# Generate synthetic data
num_samples = 600  # You can increase this number
ages = np.random.randint(20, 80, num_samples)
genders = np.random.choice(["Male", "Female"], num_samples)
blood_pressures = np.random.randint(110, 160, num_samples)
cholesterols = np.random.randint(180, 300, num_samples)
diabetes = np.random.choice([0, 1], num_samples)
disease_risks = np.random.choice(["Low", "Medium", "High"], num_samples)

# Create DataFrame
synthetic_data = pd.DataFrame({
    "age": ages,
    "gender": genders,
    "blood_pressure": blood_pressures,
    "cholesterol": cholesterols,
    "diabetes": diabetes,
    "disease_risk": disease_risks
})

# Combine with original data
df = pd.concat([df, synthetic_data], ignore_index=True)

# Save new dataset
df.to_csv("dataset/health_data_expanded.csv", index=False)

print("New dataset size:", df.shape[0])
print("health_data_expanded.csv created successfully!")
