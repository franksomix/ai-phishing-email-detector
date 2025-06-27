from transformers import pipeline

model = None

def detect_phishing(text: str) -> str:
    global model
    if model is None:
        model = pipeline(
            "text-classification",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

    try:
        results = model(text)

        if isinstance(results, list) and len(results) > 0 and "label" in results[0]:
            label = results[0]["label"]
            return "Phishing" if label == "NEGATIVE" else "Genuine"
        else:
            return "Error: Model returned unexpected result."

    except Exception as e:
        return f"Error: {str(e)}"
