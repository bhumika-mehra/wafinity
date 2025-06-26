import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="WAFinity Logs Dashboard", page_icon="📊")
st.title("📊 WAFinity - Real-Time Threat Logs")

log_file = "logs/request_log.csv"

if os.path.exists(log_file):
    df = pd.read_csv(log_file, names=["Timestamp", "Request", "Classification"])
    st.subheader("📄 Latest Logged Requests")
    st.dataframe(df.tail(25), use_container_width=True)

    st.subheader("📊 Attack Summary")
    st.bar_chart(df["Classification"].value_counts())
else:
    st.warning("No logs yet! Use the GUI or send traffic through the proxy.")
