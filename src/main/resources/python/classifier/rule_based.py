

def classify(body_text):
    """
    Rule-based content classifier.

    Applies simple heuristics or keyword-based matching to classify the input
    text into predefined categories (e.g., "product", "news", "blog").

    Parameters:
    - text (str): The content or body text to classify.

    Returns:
    - str: Predicted category label based on rules.
    """
    text = body_text.lower()
    if "toaster" in text or "kitchen" in text:
        return "E-commerce - Kitchen Appliance"
    elif "camp" in text or "outdoors" in text:
        return "Camping / Outdoor Blog"
    elif "politics" in text or "snowden" in text:
        return "News - Politics"
    return "Uncategorized"
