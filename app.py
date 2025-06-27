import streamlit as st
from phishing_detector import detect_phishing

st.set_page_config(page_title="AI Phishing Email Detector", layout="centered")

# 💡 Custom header with logo, name, background, and glowing border
st.markdown(
    """
    <style>
    .header-box {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        background-color: #e6f2ff;
        padding: 20px;
        border: 2px solid #4CAF50;
        border-radius: 15px;
        box-shadow: 0 0 15px #4CAF50;
        margin-bottom: 20px;
    }
    .header-box h1 {
        margin: 0;
        font-size: 2rem;
        color: #333;
    }
    </style>
    <div class='header-box'>
        <img src='https://raw.githubusercontent.com/franksomix/ai-phishing-email-detector/main/logo.png' width='60'/>
        <h1>AI Phishing Email Detector</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("Paste an email to detect whether it's a phishing attempt or a genuine message.")

# 📩 Email Input Form
with st.form("email_form"):
    sender = st.text_input("From:")
    subject = st.text_input("Subject:")
    body = st.text_area("Email Content")

    # ✅ Styled "Analyse" button
    st.markdown("""
        <style>
        div.stButton > button {
            background-color: #28a745;
            color: white;
            border: 2px solid #28a745;
            padding: 0.5em 2em;
            font-weight: bold;
            border-radius: 10px;
            font-size: 16px;
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
