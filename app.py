from flask import Flask, request, jsonify
import joblib
import requests
import datetime
import os
from urllib.parse import unquote

app = Flask(__name__)

# Load trained model and vectorizer
model = joblib.load('models/waf_model.joblib')
vectorizer = joblib.load('models/vectorizer.joblib')

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# Function to extract full HTTP data: headers, cookies, body
def extract_full_http_info(req):
    headers = dict(req.headers)
    cookies = req.cookies
    body = req.get_data(as_text=True)

    # Combine all into one string (normalized)
    parsed = f"HEADERS: {headers} | COOKIES: {cookies} | BODY: {unquote(body)}"
    return parsed

# API for GUI/test_request.py
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json['http_request']
    vec = vectorizer.transform([data])
    prediction = model.predict(vec)[0]

    # Log the result
    with open("logs/request_log.csv", "a") as f:
        f.write(f"{datetime.datetime.now()},{data},{'malicious' if prediction else 'benign'}\n")

    return jsonify({'classification': 'malicious' if prediction else 'benign'})

# Main proxy route (handles real HTTP traffic)
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def proxy(path):
    http_data = extract_full_http_info(request)
    vec = vectorizer.transform([http_data])
    prediction = model.predict(vec)[0]

    # Log the request
    with open("logs/request_log.csv", "a") as f:
        f.write(f"{datetime.datetime.now()},{http_data},{'malicious' if prediction else 'benign'}\n")

    # Block if malicious
    if prediction == 1:
        return "🚫 Blocked: Malicious Request", 403

    # Forward to backend (mock backend at port 5001)
    backend_url = f"http://127.0.0.1:5001/{path}"
    resp = requests.request(
        method=request.method,
        url=backend_url,
        data=request.data,
        headers=request.headers
    )

    return (resp.content, resp.status_code, resp.headers.items())

if __name__ == '__main__':
    app.run(port=8080)
