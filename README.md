
# Sentiment Analyzer Web App

This is a simple web application built with **Streamlit** that uses a **machine learning model** to analyze the sentiment of textual reviews. It classifies user input into **Positive** or **Negative** sentiment.

## 🚀 Live Demo

Check out the deployed app here: [Sentiment Analyzer Live](https://sentiment-analysis-app-8trxnvirzvc9xmiugaztcs.streamlit.app/)

## Features

- Clean and interactive UI using Streamlit.
- Preprocessing with NLTK: stopwords removal, stemming, punctuation cleaning.
- TF-IDF Vectorization.
- Sentiment classification using a trained ML model.
- Real-time predictions.

## Installation

Clone the repository:

```bash
git clone https://github.com/MallikarjunSonna/sentiment-analysis-streamlit.git
cd sentiment-analysis-streamlit
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Run Locally

```bash
streamlit run app.py
```

## File Structure

```
sentiment-analysis-streamlit/
│
├── app.py                    # Streamlit application
├── sentiment_model.pkl       # Trained sentiment classifier
├── tfidf_vectorizer.pkl      # Trained TF-IDF vectorizer
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
```

## Author

**Mallikarjun Sonna**  
Gen AI Engineer

---

Feel free to fork, contribute, and connect!
