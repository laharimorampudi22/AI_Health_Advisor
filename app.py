from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Load model and encoder
model_path = os.path.join("model", "symptom_model.pkl")
encoder_path = os.path.join("model", "label_encoder.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(encoder_path, "rb") as f:
    le = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    symptom_list = ['fever','cough','headache','body_pain','fatigue','nausea','loss_of_appetite']

    # Convert form input safely into a fixed-length binary vector
    symptoms = []
    for s in symptom_list:
        value = request.form.get(s)
        symptoms.append(1 if value else 0)

    # Predict
    pred = model.predict([symptoms])[0]
    disease_name = le.inverse_transform([pred])[0]

    advice = {
        "Flu": "Take rest, drink warm fluids, and consult a doctor if fever persists.",
        "Common Cold": "Stay hydrated, take vitamin C, and rest.",
        "Malaria": "Get tested and follow prescribed medication.",
        "Migraine": "Avoid stress and stay hydrated.",
        "Dengue": "Drink fluids, avoid NSAIDs, and rest.",
        "Food Poisoning": "Stay hydrated, eat light meals, avoid spicy foods.",
        "COVID-19": "Isolate, stay hydrated, and seek medical help if symptoms worsen.",
        "Typhoid": "Get a blood test and take antibiotics prescribed by a doctor."
    }

    return render_template('result.html', disease=disease_name, advice=advice.get(disease_name, "Consult a doctor."))

if __name__ == "__main__":
    app.run(debug=True)
