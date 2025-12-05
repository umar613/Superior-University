import re 
import string 

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")

reviews = [
    ("I really loved this movie! It was fantastic and very engaging.", "positive"),
    ("What a waste of time. The plot was boring and too predictable.", "negative"),
    ("An amazing performance by the lead actor. Great story.", "positive"),
    ("I did not enjoy the movie. It was too long and not entertaining.", "negative"),
    ("One of the best films I have seen this year. Brilliant!", "positive"),
    ("Terrible movie. I want my time back.", "negative"),
]

sentences, sentiment = zip(*reviews)

def clean_review(text):

    text = text.lower()

    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)

    words = word_tokenize(text)

    filtered = [w for w in words if w not in stopwords.words("english")]
    
    
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)


    words = word_tokenize(text)

   
    filtered = [w for w in words if w not in stopwords.words("english")]

    return " ".join(filtered)



processed_reviews = [clean_review(r) for r in sentences]

x_train, x_test, y_train, y_test = train_test_split(
    processed_reviews, sentiments, test_size=0.3, random_state=42
)

tfidf = TfidfVectorizer()
x_train_vec = tfidf.fit_transform(x_train)
x_test_vec = tfidf.transform(x_test)

model = MultinomialNB()
model.fit(x_train_vec, y_train)


y_pred = model.predict(x_test_vec)

print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("\nDetailed Report:\n", classification_report(y_test, y_pred))


test_samples = [
    "I absolutely loved the story and the acting was superb.",
    "It was a horrible experience — I hated every minute of it.",
    "Not bad, but could be better.",
    "What an incredible film! A must watch.",
    "The movie was disappointing and way too slow."
]

processed_samples = [clean_review(x) for x in test_samples]
sample_vectors = tfidf.transform(processed_samples)
preds = model.predict(sample_vectors)


for text, result in zip(test_samples, preds):
    print("\nReview:", text)
    print("Predicted Sentiment:", result)
