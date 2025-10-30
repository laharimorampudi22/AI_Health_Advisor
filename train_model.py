import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle
import os

# Load dataset
df = pd.read_csv('symptoms.csv')

# Features and target
X = df[['fever','cough','headache','body_pain','fatigue','nausea','loss_of_appetite']]
y = df['disease']

# Encode labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train model
model = RandomForestClassifier()
model.fit(X, y_encoded)

# Create model folder
os.makedirs('model', exist_ok=True)

# Save model and encoder
with open('model/symptom_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('model/label_encoder.pkl', 'wb') as f:
    pickle.dump(le, f)

print("✅ Model trained and saved successfully!")
