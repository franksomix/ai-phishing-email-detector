import streamlit as st
from phishing_detector import detect_phishing

st.set_page_config(page_title="AI Phishing Email Detector", layout="centered")

# Optional logo
st.image("logo.png", width=250)

st.title("AI Phishing Email Detector")
st.markdown("Paste an email to detect whether it's a phishing attempt or a genuine message.")

# Input form
with st.form("email_form"):
    sender = st.text_input("From:")
    subject = st.text_input("Subject:")
    body = st.text_area("Email Content")

    # Custom styled Analyze button
    custom_button = st.markdown("""
        <style>
        div.stButton > button {
            background-color: #28a745;
            color: white;
            border: 2px solid #28a745;
            padding: 0.5em 2em;
            font-weight: bold;
            border-radius: 10px;
        }
        div.stButton > button:hover {
            background-color: #218838;
            border-color: #1e7e34;
        }
        </style>
    """, unsafe_allow_html=True)

    submitted = st.form_submit_button("Analyse")

    if submitted and body.strip():
        label = detect_phishing(body)
        st.success(f"The email is: **{label}**")
