import joblib
import pandas as pd

# Load the model
model = joblib.load("models/xgboost_model.pkl")

# Function to predict fraud
def predict_fraud(transaction):
    return model.predict_proba([transaction])[0][1]

# Example prediction
transaction = [0.2, 500, 1, 0]  # Example transaction features
probability = predict_fraud(transaction)
print(f"Fraud Probability: {probability * 100:.2f}%")
