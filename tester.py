"""
Runs each question against the LLM and saves it's answers
"""
import pandas as pd
from query import answer_question

QUIZ_FILE = 'quiz2.csv'
OUTPUT_FILE = 'answered.csv'
FIELDS = ['id', 'question', 'y']

if __name__ == "__main__":
    file = pd.read_csv(QUIZ_FILE, index_col='id', dtype='str')

    for i, question in file.iterrows():
        print(f"Getting answer to question {i}... ")
        response = answer_question(question['question'])
        file.at[i, 'y'] = response
        print(response)
    file.to_csv(OUTPUT_FILE)
