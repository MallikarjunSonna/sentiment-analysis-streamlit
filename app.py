import streamlit as st
import pickle
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

# Download stopwords (if not already)
nltk.download('stopwords')

# Load model and vectorizer
model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# Text Preprocessing
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    words = text.split()
    words = [ps.stem(word) for word in words if word not in stop_words]
    return ' '.join(words)

# Streamlit App
st.title("🎯 Sentiment Analyzer")
st.subheader("Enter a review to check its sentiment")

input_text = st.text_area("Type your review here 👇")

if st.button("Predict"):
    if input_text.strip() == "":
        st.warning("Please enter a review!")
    else:
        # Preprocess and transform
        cleaned_text = clean_text(input_text)
        vectorized_text = vectorizer.transform([cleaned_text])
        prediction = model.predict(vectorized_text)[0]

        if prediction == "positive":
            st.success("✅ Positive Review")
        else:
            st.error("❌ Negative Review")
