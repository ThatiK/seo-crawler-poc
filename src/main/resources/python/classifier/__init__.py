from classifier import rule_based, ml_classifier

def classify_page(body_text, use_ml=False):
    if use_ml:
        return ml_classifier.classify(body_text)
    return rule_based.classify(body_text)
