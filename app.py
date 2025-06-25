import streamlit as st
from phishing_detector import detect_phishing

st.set_page_config(page_title="AI Phishing Email Detector", layout="centered")
st.title("📧 AI-Powered Phishing Email Detector")
st.markdown("Paste an email message below and click **Analyze Email** to check if it's safe or a phishing attempt.")

email_text = st.text_area("Enter email content:", height=250)

if st.button("Analyze Email"):
    with st.spinner("Analyzing with AI..."):
        result = detect_phishing(email_text)
    st.success(f"🔍 Prediction: **{result.upper()}**")
