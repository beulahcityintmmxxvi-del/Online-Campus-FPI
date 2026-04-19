import joblib
import os

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "svm_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "tfidf.pkl")

def classify_incident(text: str):
    if not os.path.exists(MODEL_PATH):
        # fallback before training
        return "Low", 1

    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]

    severity_map = {
        "Low": 1,
        "Medium": 2,
        "High": 3,
        "Emergency": 4
    }

    return prediction, severity_map.get(prediction, 1)
