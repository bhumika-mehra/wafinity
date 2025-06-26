# train_feedback_model.py

import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import os

# Load logs
log_path = "logs/request_log.csv"
if not os.path.exists(log_path):
    print("No feedback logs found.")
    exit()

df = pd.read_csv(log_path, names=["timestamp", "request", "label"])

# ❗ Drop empty or invalid requests
df.dropna(subset=["request", "label"], inplace=True)
df = df[df["request"].str.strip().astype(bool)]  # Remove empty strings

# Prepare features and labels
X = df["request"]
y = df["label"].map({"benign": 0, "malicious": 1})

# Vectorize
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_vec, y)

# Save new model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/waf_model.joblib")
joblib.dump(vectorizer, "models/vectorizer.joblib")

print("✅ Model updated using feedback logs!")
