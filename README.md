# 🛡️ WAFinity - Intelligent Web Application Firewall

WAFinity is a hybrid AI-powered Web Application Firewall that protects web applications using static signature-based filtering, dynamic anomaly detection, and feedback-driven adaptive learning. It includes a real-time dashboard for monitoring threats.

---

## 🎯 Features

✅ Detects and blocks malicious HTTP requests (SQLi, XSS, CSRF, etc.)  
✅ Uses trained ML models to classify traffic as `benign` or `malicious`  
✅ Logs all request activity with timestamps  
✅ Real-time bar chart & logs using Streamlit  
✅ Modular backend: async proxy, dummy backend server, and model server  
✅ Adaptive learning through feedback model retraining  
✅ Deployable to cloud or container platforms

---

## 🖥️ WAFinity Dashboard

📍 **Location:** `waf_gui.py`  
📍 **Framework:** Streamlit

### 🚀 Launch Dashboard

```bash
streamlit run waf_gui.py
