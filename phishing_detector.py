from transformers import pipeline

model = None

def detect_phishing(text: str) -> str:
    global model
    if model is None:
        model = pipeline(
            "text-classification",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )
    
    results = model(text)
    
    # Get the first prediction result
    result = results[0]
    label = result["label"]

    # Map sentiment to phishing/genuine for demo
    if label == "NEGATIVE":
        return "Phishing"
    else:
        return "Genuine"
