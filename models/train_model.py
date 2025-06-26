from sklearn.ensemble import IsolationForest
import joblib

def train(X):
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(X)
    joblib.dump(model, 'models/waf_model.joblib')
