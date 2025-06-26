from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

def train_vectorizer(data):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(data)
    joblib.dump(vectorizer, 'models/vectorizer.joblib')
    return X
