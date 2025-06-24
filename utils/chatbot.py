# utils/chatbot.py
import pandas as pd
from difflib import get_close_matches
import re

# Load CSV
def load_chatbot_data(filepath="data/farmer_chatbot_qa.csv"):
    try:
        df = pd.read_csv(filepath)
        if 'question' not in df.columns or 'answer' not in df.columns:
            raise ValueError("CSV must have 'question' and 'answer' columns.")
        return df
    except Exception as e:
        print(f"Error loading chatbot data: {e}")
        return pd.DataFrame(columns=['question', 'answer'])

def get_answer(user_question, df):
    if df.empty:
        return " Chatbot data is unavailable."

    user_question = user_question.lower().strip()

    greetings = ['hi', 'hello', 'hey', 'hii', 'hai']
    thanks = ['thanks', 'thank you', 'thx', 'thank u']
    if user_question in greetings:
        return " Hi there! How can I assist you with farming today?"
    if user_question in thanks:
        return " You're welcome! Let me know if you have more farming questions."

    exact = df[df['question'].str.lower() == user_question]
    if not exact.empty:
        return exact.iloc[0]['answer']

    keywords = user_question.split()
    for word in keywords:

        keyword_match = df[df['question'].str.lower().str.contains(fr'\b{re.escape(word)}\b', regex=True)]
        if not keyword_match.empty:
            return keyword_match.iloc[0]['answer']

    # Check for one-word category or crop queries
    word_matches = df[df['question'].str.lower().str.contains(user_question)]
    if not word_matches.empty:
        return word_matches.iloc[0]['answer']

    # Fuzzy matching
    questions = df['question'].str.lower().tolist()
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    if matches:
        return df[df['question'].str.lower() == matches[0]].iloc[0]['answer']

    return "🤔 Sorry, I couldn't understand that. Try rephrasing or ask another farming-related question."
