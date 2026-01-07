from model import detoxify_predict
from rule_engine import apply_rules

def classify_comment(comment: str):

    # 1. Rule-based dulu
    rule_result = apply_rules(comment)

    if rule_result is not None:
        category, bully_type, detected_by, confidence = rule_result
        return {
            "original": comment,
            "translated": comment,   # rule tidak translate
            "category": category,
            "type": bully_type,
            "detected_by": detected_by,
            "confidence": confidence
        }

    # 2. Jika rule tidak mendeteksi → pakai Detoxify
    category, bully_type, detected_by, confidence, translated = detoxify_predict(comment)

    return {
        "original": comment,
        "translated": translated,
        "category": category,
        "type": bully_type,
        "detected_by": detected_by,
        "confidence": confidence
    }
