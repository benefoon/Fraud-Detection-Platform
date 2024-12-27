import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib

# Load dataset
data = pd.read_csv("data/train.csv")

# Preprocess data
X = data.drop("is_fraud", axis=1)
y = data["is_fraud"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = XGBClassifier(n_estimators=100, max_depth=5, learning_rate=0.1)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "models/xgboost_model.pkl")
