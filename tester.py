"""
Runs each question against the LLM and saves it's answers
"""
import pandas as pd
from query import answer_question
from loader import get_relevant_info

QUIZ_FILE = 'quiz.csv'
OUTPUT_FILE = 'answered.csv'
FIELDS = ['id', 'question', 'y']

if __name__ == "__main__":
    file = pd.read_csv(QUIZ_FILE, index_col='id', dtype='str')

    for i, question in file.iterrows():
        print(f"Getting answer to question {i + 1}... ")
        relevant_docs = get_relevant_info(question['question'])
        file.at[i, 'y'] = answer_question(question['question'])

    file.to_csv(OUTPUT_FILE)
