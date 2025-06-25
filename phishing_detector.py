from transformers import pipeline

# Load pre-trained model from Hugging Face
classifier = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-phishing")

def detect_phishing(text):
    result = classifier(text)[0]
    return result['label']
