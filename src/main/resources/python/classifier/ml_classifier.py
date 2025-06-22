from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

train_texts = [
    "buy this amazing toaster",
    "outdoors is beautiful for camping",
    "politics and the snowden leak",
]
train_labels = ["ecommerce", "blog", "news"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(train_texts)

model = MultinomialNB()
model.fit(X, train_labels)

def classify(body_text):
    """
    Classify text content using a simple ML model (TF-IDF + Naive Bayes).

    This function applies a basic machine learning pipeline to categorize 
    input content into high-level types (e.g., product, blog, news, etc.).

    The pipeline includes:
    - TF-IDF vectorization: Transforms raw text into numerical feature vectors
      by measuring how important each word is within the corpus.
    - Multinomial Naive Bayes: A probabilistic classifier trained on labeled
      examples, effective for text classification tasks.

    Parameters:
    - body_text (str): Raw page body text to classify.

    Returns:
    - str: Predicted category label for the input text.
    """
    X_test = vectorizer.transform([body_text])
    return model.predict(X_test)[0]
