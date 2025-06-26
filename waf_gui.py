import streamlit as st
import joblib
import pandas as pd
import os

# Load model and vectorizer
model = joblib.load('models/waf_model.joblib')
vectorizer = joblib.load('models/vectorizer.joblib')

# Set Streamlit page config
st.set_page_config(page_title="WAFinity Dashboard", layout="wide")
st.title("🛡️ WAFinity - Real-Time Web Application Firewall Logs")

# Section: Analyze New HTTP Request
st.subheader("📥 HTTP Request Analyzer")
user_input = st.text_area("Paste your HTTP Request:")

if st.button("Analyze"):
    if user_input.strip():
        vec = vectorizer.transform([user_input])
        prediction = model.predict(vec)[0]
        label = "🚨 Malicious" if prediction == -1 else "✅ Benign"

        st.success(f"Classification: {label}")

        # Save to logs
        os.makedirs("logs", exist_ok=True)
        with open("logs/request_log.csv", "a") as f:
            clean_input = user_input.replace(",", " ").replace("\n", " ")
            f.write(f"{pd.Timestamp.now()},{clean_input},{'malicious' if prediction else 'benign'}\n")

        # Set refresh flag
        st.session_state["refresh_logs"] = True
    else:
        st.warning("Please paste an HTTP request before analyzing.")

# Section: Live Logs
st.subheader("📊 Attack Distribution & Recent Logs")
log_path = "logs/request_log.csv"

if os.path.exists(log_path):
    df = pd.read_csv(log_path, names=["timestamp", "request", "label"])

    # Plot bar chart
    chart_data = df["label"].value_counts()
    st.bar_chart(chart_data)

    # Show last 5 logs
    st.markdown("### 📝 Last 5 Requests")
    st.dataframe(df.tail(5).sort_values(by="timestamp", ascending=False), use_container_width=True)
else:
    st.info("No logs yet. Analyze a request above to generate data.")

# Optional: Manual Refresh
if st.button("🔁 Refresh Logs"):
    st.experimental_rerun()
