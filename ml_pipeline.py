import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
import joblib

# Load the dataset containing transactions
data = pd.read_csv('transactions.csv')

# Prepare features (X) and target (y)
X = pd.get_dummies(data.drop('is_fraud', axis=1), drop_first=True)
y = data['is_fraud']

# Data Preprocessing: Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Balance the dataset using SMOTE (Synthetic Minority Over-sampling Technique)
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model on the training data
model.fit(X_train, y_train)

# Evaluate the model on the test data
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))  # Detailed classification metrics
print("ROC AUC:", roc_auc_score(y_test, model.predict_proba(X_test)[:, 1]))  # Area under the ROC curve

# Save the model for future use
joblib.dump(model, 'fraud_detection_model.pkl')
joblib.dump(scaler, 'scaler.pkl')  # Save the scaler for future transformations
