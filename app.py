import streamlit as st
from phishing_detector import detect_phishing

st.set_page_config(page_title="AI Phishing Email Detector", layout="centered")
st.title("📧 AI-Powered Phishing Email Detector")
st.markdown("Paste a suspicious email below and tap **Analyze Email**.")

email = st.text_area("Email content:", height=250)

if st.button("Analyze Email"):
    if not email.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing with AI…"):
            label = detect_phishing(email)
        st.success(f"🔍 Result: **{label.upper()}**")
