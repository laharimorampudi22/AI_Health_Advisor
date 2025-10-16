import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv('data/symptoms.csv')
X = data.drop('disease', axis=1)
y = data['disease']

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open('model/symptom_model.pkl', 'wb'))
print("✅ Model trained and saved!")

