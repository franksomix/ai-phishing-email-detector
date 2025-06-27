from transformers import pipeline

model = None

def detect_phishing(text: str) -> dict:
    global model
    if model is None:
        model = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-phishing")
    result = model(text)[0]
    return {
        "label": result["label"],  # SPAM or HAM
        "confidence": round(result["score"] * 100, 2)
    }
