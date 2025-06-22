

def classify(body_text):
    text = body_text.lower()
    if "toaster" in text or "kitchen" in text:
        return "E-commerce - Kitchen Appliance"
    elif "camp" in text or "outdoors" in text:
        return "Camping / Outdoor Blog"
    elif "politics" in text or "snowden" in text:
        return "News - Politics"
    return "Uncategorized"
