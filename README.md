# 🧠 Medical QA Chatbot using MedQuAD Dataset

This project is an intelligent QA (Question Answering) chatbot built using the [MedQuAD]dataset from the U.S. National Library of Medicine. It uses **TF-IDF vectorization** and **cosine similarity** to retrieve relevant answers from medical question-answer pairs.

---

## 📦 Features

- Loads and parses XML-based medical QA data.
- Uses `scikit-learn` for vectorizing and similarity matching.
- Interactive interface with **Streamlit**.
- Answers user queries by finding the closest matching question.

---

## 🛠️ How it works

1. **Data Parsing**: Extracts `<Question>` and `<Answer>` tags from MedQuAD XML files.
2. **Preprocessing**: Uses `TfidfVectorizer` to convert questions to numerical vectors.
3. **Similarity**: Uses `cosine_similarity` to find the most relevant existing question.
4. **Response**: Displays the best matching question and answer to the user.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/medquad-qa-chatbot.git
cd medquad-qa-chatbot
