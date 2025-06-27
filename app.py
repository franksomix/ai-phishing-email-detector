import streamlit as st
from phishing_detector import detect_phishing

st.set_page_config(page_title="AI Phishing Email Detector", layout="centered")

# Optional logo
st.image("logo.png", width=180)

st.title("AI Phishing Email Detector")
st.markdown("Paste an email to detect whether it's a phishing attempt or a genuine message.")

# Input form
with st.form("email_form"):
    sender = st.text_input("From:")
    subject = st.text_input("Subject:")
    body = st.text_area("Email Content")

    submitted = st.form_submit_button("Detect")

    if submitted and body.strip():
        label = detect_phishing(body)
        st.success(f"The email is: **{label}**")
