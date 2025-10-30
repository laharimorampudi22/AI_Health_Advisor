@app.route('/predict', methods=['POST'])
def predict():
    # Define all possible symptoms in the same order used for training
    symptom_list = ['fever', 'cough', 'headache', 'body_pain', 'fatigue', 'nausea', 'loss_of_appetite']

    # Create a binary vector for all symptoms (1 = checked, 0 = unchecked)
    symptoms = []
    for s in symptom_list:
        value = request.form.get(s)
        if value:
            symptoms.append(1)
        else:
            symptoms.append(0)

    # ✅ Ensure input length matches model expectation
    if len(symptoms) != 7:
        return f"Error: Expected 7 symptoms, got {len(symptoms)}."

    # Predict using the model
    pred = model.predict([symptoms])[0]
    disease_name = le.inverse_transform([pred])[0]

    advice = {
        "Flu": "Take rest, drink warm fluids, and consult a doctor if fever persists.",
        "Common Cold": "Stay hydrated, t
