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
    X_test = vectorizer.transform([body_text])
    return model.predict(X_test)[0]
