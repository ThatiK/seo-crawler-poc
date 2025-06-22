import os
import nltk
from collections import Counter
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords

# Use project-local nltk_data
NLTK_DATA_PATH = os.getenv("NLTK_DATA", os.path.abspath("nltk_data"))
nltk.data.path.append(NLTK_DATA_PATH)

def ensure_nltk_resources():
    try:
        nltk.data.find("corpora/stopwords")
    except LookupError:
        nltk.download("stopwords", download_dir=NLTK_DATA_PATH)

ensure_nltk_resources()

def extract_topics(body_text, top_n=5):
    tokenizer = TreebankWordTokenizer()
    stop_words = set(stopwords.words("english"))
    words = tokenizer.tokenize(body_text.lower())
    filtered = [w for w in words if w.isalpha() and w not in stop_words]
    freq = Counter(filtered)
    return [word for word, count in freq.most_common(top_n)]
