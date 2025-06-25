# AI-Powered Phishing Email Detector

This project is built by **Francis Ezeanyino** as part of the 3MTT Cohort 3 Showcase. It uses an AI model from Hugging Face to classify email messages as "phishing" or "safe".

## How It Works

- You paste an email into the app.
- The model analyzes the content.
- It returns whether it's a phishing email or a legitimate one.

## Files Included

- `app.py`: Streamlit interface
- `phishing_detector.py`: AI model loading and prediction
- `requirements.txt`: Required Python packages
- `examples/`: Sample test emails

## Running the App

```bash
pip install -r requirements.txt
streamlit run app.py
```
