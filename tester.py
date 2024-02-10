"""
Runs each question against the LLM and saves it's answers
"""
import pandas as pd
from query import answer_question

QUIZ_FILE = 'quiz.csv'
OUTPUT_FILE = 'answered.csv'
FIELDS = ['id', 'question', 'y']

if __name__ == "__main__":
    file = pd.read_csv(QUIZ_FILE, index_col='id')

    for i, question in file.iterrows():
        file.at[i, 'y'] = answer_question(question['question'])

    file.to_csv(OUTPUT_FILE)
