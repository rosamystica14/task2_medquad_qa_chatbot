import streamlit as st
from data_loader import extract_question_and_answer
from qa_system import MedicalQASystem

st.markdown(
    """
    <style>
    /*page background*/
    .stApp{
        background-color:fefefe;
        font-family:'segoe UI',sans-serif;
        padding:10px;
    }
    /*title styling*/
    h1{
        color:#2c3E50;
        text-align:center;
    }
    /*Input Box*/
    input [type="text"]{
        border: 2px solid #2980B9;
        padding:10px;
        border-radius:5px;
    }
    /*Output Area*/
    .stMarkdown{
        background-color:#ECF0F1;
        padding:20px;
        border-radius:10px;
        font-size:16px;
    }
    /*Emoji size fix*/
    .emoji{
        font-size:24px;
        margin-right:5px;
    }
    </style>
    """,
    unsafe_allow_html= True
)

# Function to extract question-answer antries from all xml files
@st.cache_data
def load_data():
    base_path = r"C:/Users/rosaa/Downloads/MedQuAD-master/MedQuAD-master/"
    return extract_question_and_answer(base_path)

# Set Page Config
st.set_page_config(page_title="🩺 MedQBot - Medical Q&A", page_icon="💊")

st.title("🩺 MedBot - AI Powered Medical Assistent 🤖")
st.write("Welcome! Ask any medical-related question and get answers powered by trusted sources.")

# Load data
qa_data = load_data()
qa_bot = MedicalQASystem(qa_data)

# User Input
user_question = st.text_input("❓ Enter your question here:")

if user_question:
    with st.spinner("Searching for the best answer..."):
        results = qa_bot.fetch_relevant_answer(user_question)
        if results:
            st.success("🔍 Matched Question:")
            st.markdown(f"**{results[0]['matched_question']}**")
            st.info(f"💬 Answer:\n\n{results[0]['answer']}")
        else:
            st.warning("Sorry 😔 no relevant answer found.")
