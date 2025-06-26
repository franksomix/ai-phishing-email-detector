import streamlit as st
from phishing_detector import detect_phishing

st.set_page_config(page_title="AI Phishing Email Detector")

st.title("📧 AI Email Analyzer")
st.write("Enter an email message below to check if it's potentially phishing or not:")

email = st.text_area("Paste email content here...")

if st.button("Analyze Email"):
    if email:
        result = detect_phishing(email)
        if result == "NEGATIVE":
            st.success("✅ This email is likely safe.")
        else:
            st.error("🚨 Warning! This email may be phishing.")
    else:
        st.warning("Please enter some email content first.")
