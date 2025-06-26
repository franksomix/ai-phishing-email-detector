from transformers import pipeline

model = None

def detect_phishing(text: str) -> str:
    global model
    if model is None:
        model = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-phishing")
    result = model(text)[0]
    return result["label"]
