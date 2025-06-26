from transformers import pipeline

model = None

def detect_phishing(text: str) -> str:
    global model
    if model is None:
        model = pipeline("text-classification", model="bhadresh-savani/bert-base-uncased-emotion")
    result = model(text)[0]
    return result["label"]
