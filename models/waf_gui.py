import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
import os

# Load model and vectorizer
model = joblib.load('models/waf_model.joblib')
vectorizer = joblib.load('models/vectorizer.joblib')

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

st.set_page_config(page_title="WAFinity Dashboard", page_icon="🛡️")
st.title("🛡️ WAFinity - Intelligent Web Application Firewall")
st.markdown("Analyze HTTP requests in real time and visualize threat patterns 📊")

# 📥 HTTP Request Input
user_input = st.text_area("Paste an HTTP Request to Analyze")

if st.button("Analyze"):
    vec = vectorizer.transform([user_input])
    prediction = model.predict(vec)[0]
    label = "🚨 Malicious" if prediction else "✅ Benign"
    st.success(f"Classification: {label}")

    # ✅ Log the result
    with open("logs/request_log.csv", "a") as f:
        cleaned_input = user_input.replace(",", " ")  # avoid CSV breakage
        f.write(f"{datetime.now()},{cleaned_input},{'malicious' if prediction else 'benign'}\n")

st.divider()
st.subheader("📊 Live Traffic Overview")

# Load and display logs
try:
    df = pd.read_csv("logs/request_log.csv", header=None, names=["Time", "Request", "Classification"])

    # 🔢 Bar Chart: Benign vs Malicious
    st.markdown("### Attack Classification Summary")
    chart_data = df["Classification"].value_counts()
    st.bar_chart(chart_data)

    # 🧾 Recent Logs Table
    st.markdown("### 🧾 Last 5 Requests")
    st.dataframe(df.tail(5).sort_values("Time", ascending=False), use_container_width=True)

    # 🔁 Refresh Button
    if st.button("🔁 Refresh Logs"):
        st.rerun()

except FileNotFoundError:
    st.warning("⚠️ No log data found yet. Use the Analyze button above first.")
