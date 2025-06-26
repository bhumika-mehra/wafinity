🛡️ WAFinity - Intelligent Web Application Firewall
WAFinity is a Machine Learning-powered Web Application Firewall designed to detect and block OWASP Top 10 threats and zero-day attacks with minimal manual configuration. It integrates real-time HTTP traffic monitoring, adaptive ML filtering, deep packet inspection, and a live dashboard for full-stack application protection.

🌐 Features
🔍 Signature + Anomaly Detection (Hybrid WAF engine)

🧠 ML-based classification of HTTP requests (benign/malicious)

📊 Interactive Streamlit dashboard for live threat monitoring

⚡ Asynchronous proxy architecture for low-latency performance

🔄 Feedback-driven model training for reducing false positives

☁️ Cloud-native ready with modular, scalable components

🚀 Project Architecture
bash
wafinity/
├── models/
│   ├── waf_model.joblib           # Trained ML model
│   ├── vectorizer.joblib          # TF-IDF vectorizer
│   └── train_model.py             # Model training script
├── preprocessing/
│   └── vectorizer.py              # Preprocessing logic
├── async_proxy.py                 # Asynchronous proxy WAF server
├── dummy_backend.py              # Mock backend service
├── waf_gui.py                     # Streamlit dashboard
├── train_all.py                   # Full training pipeline
├── test_request.py                # Manual test request
├── test_proxy_request.py          # Proxy test request
├── train_feedback_model.py        # Adaptive re-training
├── logs/
│   └── request_log.csv            # Real-time threat logs
├── requirements.txt
└── README.md

🖥️ Dashboard Preview
The WAFinity dashboard includes:

✅ HTTP Request Analyzer

📈 Live attack distribution bar chart

📝 Recent request logs

🔁 Refresh/Analyze features in-browser

Run:

bash
streamlit run waf_gui.py
Access at: http://localhost:8501

⚙️ Installation & Setup

1. Clone the Repository
bash
git clone https://github.com/bhumika-mehra/wafinity.git
cd wafinity

2. Create & Activate Virtual Environment
bash
python -m venv venv
venv\Scripts\activate      # On Windows

3. Install Dependencies
bash

pip install -r requirements.txt

🧠 Model Training

Train from Scratch
bash
python train_model.py

Train All (Preprocessing + Model)
bash
python train_all.py

🔐 Run WAF Proxy (Async)
Start Dummy Backend
bash
python dummy_backend.py

Start WAF Proxy
bash
python async_proxy.py
Runs on: http://127.0.0.1:9090

Test with Payload
bash
python test_proxy_request.py

🔁 Adaptive Feedback Training
bash
python train_feedback_model.py

This retrains the model using real log data (logs/request_log.csv).

✅ Project Goals Achieved
✅ Enhanced Application Security
ML + DPI + Signature filters defend against OWASP Top 10 (SQLi, XSS, etc.)

✅ Efficient Network Performance
Uses async proxy + token bucket rate limiting

✅ Reduced False Positives
Adaptive feedback training from real logs

✅ Proactive Defense System
Classifies, blocks, and logs malicious requests in real-time

✅ Secure & Scalable Deployment
Modular sockets + REST + Streamlit integration; cloud-deployable

📌 Methodology Followed
Signature-Based Detection — Static rules for known threats

ML-Based Anomaly Detection — IsolationForest classifier

Deep Packet Inspection (DPI) — Full HTTP payload + headers

Real-Time Monitoring — Async I/O + rate limiting

Modular Architecture — Socket & REST-based async proxy

Feedback Learning — Re-train using logged predictions

👩‍💻 Author
Bhumika Mehra
WAFinity Project | 2025
GitHub: @bhumika-mehra# Sansio

