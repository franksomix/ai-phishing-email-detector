 AI Phishing Email Detector

This is an AI-powered phishing detection tool built using Streamlit and Hugging Face Transformers. It analyzes the content of emails and classifies them as either **Phishing** or **Genuine**, helping users avoid scams.

![App Logo](https://raw.githubusercontent.com/franksomix/ai-phishing-email-detector/main/logo.png)

---

## 💡 What It Does

- ✅ Takes in email sender, subject, and content
- 🧠 Uses a pre-trained AI model to classify the email
- 💬 Returns whether it's a **Phishing** or **Genuine** message
- 🌐 Runs fully online – no download or login required
- 🎨 Designed with a glowing header, green “Analyse” button, and professional branding

---

## 🚀 Live Demo

👉 Click here to use the app now:  
🔗 **[https://franksomix-ai-phishing-email-detector.streamlit.app](https://franksomix-ai-phishing-email-detector.streamlit.app)**

---

## 🧠 How It Works

- The app uses the **DistilBERT** model from Hugging Face
- It performs **sentiment analysis** to determine intent
- If the email content is **Negative** → it's labeled **Phishing**  
- If the content is **Positive** → it's labeled **Genuine**

_Note: This logic is simplified for demo purposes and will be upgraded later using phishing-specific datasets._

---

## 🧪 Sample Emails

### ✅ Genuine Email

Hello Francis, your interview is scheduled for Thursday. Let us know if you’re available.

### ❌ Phishing Email

URGENT: Your bank account has been suspended. Click http://fakebank.com to restore access.

---

## 📦 Technologies Used

| Tool             | Purpose                         |
|------------------|----------------------------------|
| Streamlit        | UI and Web App Framework        |
| Hugging Face Transformers | AI Model for Classification |
| Python           | Backend Logic                   |
| GitHub + Streamlit Cloud | Hosting & Version Control |

---

## 📂 File Structure

```bash
📁 ai-phishing-email-detector/
├── app.py                 # Main Streamlit app UI
├── phishing_detector.py   # Phishing detection logic using Hugging Face
├── logo.png               # Custom branded logo
└── README.md              # Project documentation

---

## 🙋 About the Creator 

👨‍💻 Name: Francis Ezeanyino
🧭 3MTT, Cybersecurity Pathway, Cohort 3 fellow 
🌍 GitHub Profile: franksomix


---
## 📌 Future Plans

🔐 Train with actual phishing datasets for greater accuracy

🧠 Integrate a confidence score with model output

📬 Allow users to upload .eml files or email screenshots

🌍 Build a dashboard for organizations to use it internally



---

Thanks for checking out this project!
If you like it, feel free to ⭐ the repo and share!
