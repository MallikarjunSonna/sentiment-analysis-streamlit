# 🧠 Sentiment Analysis Web App

This project is a **Sentiment Analyzer** built using **Machine Learning** and **Streamlit**. It classifies user‑submitted text reviews as either **Positive** ✅ or **Negative** ❌ based on trained data.

---

## 🔍 Overview
- **Input**: Any English text (e.g., product or movie review).
- **Pre‑processing**: Lower‑casing, punctuation & stop‑word removal, stemming.
- **Vectorization**: TF‑IDF.
- **Model**: Trained Logistic Regression.
- **Interface**: Streamlit web app.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `Sentiment_Analysis.ipynb` | Notebook with EDA, training, and model saving |
| `app.py` | Streamlit web interface |
| `sentiment_model.pkl` | Trained classifier |
| `tfidf_vectorizer.pkl` | Fitted TF‑IDF vectorizer |
| `dataset.csv` | Training dataset |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation (this file) |

---

## 🛠 How to Run Locally

```bash
# 1. clone repo
git clone https://github.com/your‑username/sentiment‑analysis‑app.git
cd sentiment‑analysis‑app

# 2. (optional) create & activate venv
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. install requirements
pip install -r requirements.txt

# 4. launch
streamlit run app.py
```

Open **http://localhost:8501/** in your browser.

---

## 🧠 Tech Stack
- Python 3.10  
- Streamlit 1.45  
- scikit‑learn 1.6  
- NLTK 3.9  
- pandas / numpy

---

## 🧪 Sample Inputs

| Review | Prediction |
|--------|------------|
| *“I love this product, works perfectly!”* | ✅ Positive |
| *“Terrible quality. Very disappointed.”* | ❌ Negative |

---

## 🚀 Future Work
- Deploy on Streamlit Cloud or HuggingFace Spaces  
- Show model confidence score  
- Add Neutral sentiment class  
- Upgrade to transformer‑based embeddings

---

## 👤 Author
**Mallikarjun Sonna**  
_Data Science Intern @ Unified Mentor Pvt. Ltd._  
📧 mallusonna43@gmail.com  
🔗 <https://www.linkedin.com/in/mallikarjun-sonna>
