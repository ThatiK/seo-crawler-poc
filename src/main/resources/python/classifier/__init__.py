from classifier import rule_based, ml_classifier

def classify_page(body_text, use_ml=False):
    """
    Unified classification interface.

    Delegates to either the rule-based or ML-based classifier based on the flag.

    Parameters:
    - body_text (str): The body text to classify.
    - use_ml (bool): If True, use ML model; otherwise, use rule-based.

    Returns:
    - str: Predicted category.
    """
    if use_ml:
        return ml_classifier.classify(body_text)
    return rule_based.classify(body_text)
