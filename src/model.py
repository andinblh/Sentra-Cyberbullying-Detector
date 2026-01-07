from detoxify import Detoxify
from deep_translator import GoogleTranslator

# Load model Detoxify Multilingual
model = Detoxify("multilingual")

translator = GoogleTranslator(source="auto", target="en")

def translate_to_en(text: str):
    try:
        return translator.translate(text)
    except:
        return text


def map_scores_to_category(scores: dict, threshold=0.35):
    # Ambil label tertinggi
    max_label = max(scores, key=scores.get)
    max_value = float(scores[max_label])

    mapping = {
        "toxicity": "toxic",
        "severe_toxicity": "severe_toxic",
        "insult": "insult",
        "identity_attack": "identity_attack",
        "obscene": "obscene",
        "threat": "threat",
        "sexual_explicit": "sexual",
    }

    bully_type = mapping.get(max_label, "toxic")

    if max_value >= threshold:
        category = "Bullying"
    else:
        category = "Non-bullying"
        bully_type = "-"

    return category, bully_type, "detoxify", max_value


def detoxify_predict(text: str, threshold=0.35):
    translated = translate_to_en(text)

    scores = model.predict(translated)

    category, bully_type, detected_by, confidence = map_scores_to_category(scores, threshold)

    return category, bully_type, detected_by, confidence, translated
