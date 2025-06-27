from transformers import pipeline

model = None

def detect_phishing(text: str) -> str:
    global model
    if model is None:
        model = pipeline(
            "text-classification",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )
    
    result = model(text)[0]
    label = result["label"]

    # Translate model's output to phishing/genuine
    if label == "NEGATIVE":
        return "Phishing"
    else:
        return "Genuine"
