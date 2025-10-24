import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import numpy as np
import os

# Example synthetic training data (7 symptoms × 8 diseases)
X = np.array([
    [1,1,1,0,1,0,0],  # Flu
    [1,1,0,0,1,0,0],  # Common Cold
    [1,0,0,1,1,0,0],  # Malaria
    [0,0,1,0,1,0,0],  # Migraine
    [1,1,1,1,1,1,0],  # Dengue
    [0,0,0,1,1,1,1],  # Food Poisoning
    [1,1,1,1,1,1,0],  # COVID-19
    [1,1,1,1,1,0,0],  # Typhoid
])

# Disease labels
y = np.array([
    "Flu", "Common Cold", "Malaria", "Migraine",
    "Dengue", "Food Poisoning", "COVID-19", "Typhoid"
])

# Encode disease labels as numbers
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train a simple logistic regression model
model = LogisticRegression()
model.fit(X, y_encoded)

# Create the 'model' folder if it doesn't exist
os.makedirs("model", exist_ok=True)

# Save model and encoder as .pkl files
with open("model/symptom_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model/label_encoder.pkl", "wb") as f:
    pickle.dump(le, f)

print("✅ Model and encoder saved successfully in /model folder.")
