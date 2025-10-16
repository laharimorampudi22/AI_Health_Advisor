from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model/symptom_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    symptoms = [int(request.form.get(symptom, 0)) for symptom in ['fever','cough','headache','body_pain']]
    prediction = model.predict([symptoms])[0]
    
    # Personalized advice
    advice = {
        "Flu": "Take rest, drink warm fluids, and consult doctor if fever persists.",
        "Common Cold": "Stay hydrated, take vitamin C, and get enough sleep.",
        "Malaria": "Seek immediate medical attention and get tested."
    }
    return render_template('result.html', disease=prediction, advice=advice.get(prediction, "Consult a doctor."))

if __name__ == '__main__':
    app.run(debug=True)

