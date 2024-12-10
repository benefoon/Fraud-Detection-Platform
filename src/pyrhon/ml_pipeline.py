import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from cryptography.fernet import Fernet
import numpy as np
import matplotlib.pyplot as plt

# ---- Security: Data Encryption and Masking ----

# Generate a key for encryption (store it securely)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypting sensitive data (example: customer_card_number)
def encrypt_data(data):
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Mask sensitive data for display (example: card number masking)
def mask_data(data):
    return data[:4] + " **** **** " + data[-4:]

# Example of encrypting and masking
encrypted_card = encrypt_data("1234567890123456")
masked_card = mask_data("1234567890123456")
print(f"Encrypted Card: {encrypted_card}")
print(f"Masked Card: {masked_card}")

# ---- Data Preprocessing ----

# Load data
data = pd.read_csv('data/sample_transactions.csv')

# Feature selection and scaling
scaler = StandardScaler()
data[['amount', 'time']] = scaler.fit_transform(data[['amount', 'time']])

# Handle imbalanced dataset using SMOTE
smote = SMOTE()
X_resampled, y_resampled = smote.fit_resample(data.drop('fraudulent', axis=1), data['fraudulent'])

# ---- Model Training with Hyperparameter Tuning ----

# Define model
model = RandomForestClassifier()

# Hyperparameter tuning using GridSearchCV
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, n_jobs=-1)
grid_search.fit(X_resampled, y_resampled)

best_model = grid_search.best_estimator_

# ---- Model Evaluation ----
from sklearn.metrics import classification_report, roc_auc_score

# Evaluate the best model
y_pred = best_model.predict(X_resampled)
print(classification_report(y_resampled, y_pred))

# Evaluate using ROC AUC score
roc_auc = roc_auc_score(y_resampled, best_model.predict_proba(X_resampled)[:, 1])
print(f"ROC AUC: {roc_auc}")

# ---- Feature Importance Visualization ----
importances = best_model.feature_importances_
plt.barh(data.drop('fraudulent', axis=1).columns, importances)
plt.xlabel("Feature Importance")
plt.title("Feature Importance of Model")
plt.show()
