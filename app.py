import streamlit as st
from PIL import Image
logo = Image.open("logo.png")
col1, col2 = st.columns([1, 5])
with col1:
    st.image(logo, width=120)
from phishing_detector import detect_phishing

st.set_page_config(page_title="AI Phishing Email Detector", layout="centered")

st.title("AI Phishing Email Detector")
st.write("Paste an email to detect whether it's a phishing attempt or a genuine message.")

# Structured input form
sender = st.text_input("From:", placeholder="e.g. service@securebank.com")
subject = st.text_input("Subject:", placeholder="e.g. Urgent: Verify Your Account")
body = st.text_area("Email Content", height=250, placeholder="Paste the body of the email here...")

if st.button("Analyze Email"):
    if body:
        with st.spinner("Analyzing with AI..."):
            result = detect_phishing(body)
            label = result["label"]
            confidence = result["confidence"]

            if label.upper() == "SPAM":
                st.error(f"🚨 This is likely a **Phishing Email** ({confidence}% confidence)")
            else:
                st.success(f"✅ This email appears **Safe** ({confidence}% confidence)")
    else:
        st.warning("Please enter email content before clicking Analyze.")
