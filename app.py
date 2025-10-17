@app.route('/predict', methods=['POST'])
def predict():
    # List of all symptoms
    symptom_list = ['fever','cough','headache','body_pain','fatigue','nausea','loss_of_appetite']
    
    # Convert form inputs to integers safely (0 if unchecked)
    symptoms = []
    for s in symptom_list:
        value = request.form.get(s)
        if value is None:
            value = 0
        symptoms.append(int(value))
    
    # Predict disease
    pred = model.predict([symptoms])[0]
    disease_name = le.inverse_transform([pred])[0]

    # Personalized advice
    advice = {
        "Flu": "Take rest, drink warm fluids, and consult doctor if fever persists.",
        "Common Cold": "Stay hydrated, take vitamin C, and rest.",
        "Malaria": "Get tested and follow prescribed medication.",
        "Migraine": "Avoid stress and stay hydrated.",
        "Dengue": "Drink fluids, avoid NSAIDs, and rest.",
        "Food Poisoning": "Stay hydrated, eat light, avoid spicy foods.",
        "COVID-19": "Isolate, stay hydrated, and seek medical help if symptoms worsen.",
        "Typhoid": "Get a blood test and take antibiotics prescribed by doctor."
    }

    return render_template('result.html', disease=disease_name, advice=advice.get(disease_name, "Consult a doctor."))
