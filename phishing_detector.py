from transformers import pipeline

model = None

def detect_phishing(text: str) -> str:
    global model
    if model is None:
        # Using a public model that doesn't require authentication
        model = pipeline(
            "text-classification",
            model="mohsenfayyaz/phishing-email-detector-bert"
        )
    result = model(text)[0]
    return result["label"]
