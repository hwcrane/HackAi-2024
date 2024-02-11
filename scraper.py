import os
os.environ["GOOGLE_CSE_ID"] = "37f4c213488a841eb"
os.environ["GOOGLE_API_KEY"] = "AIzaSyDF4WSCuiWjHnFNooSLn-B4crM5oqfLUd0"

from langchain.tools import Tool
from langchain_community.utilities import GoogleSearchAPIWrapper

search = GoogleSearchAPIWrapper()

tool = Tool(
    name="Google Search",
    description="Search Google for recent results",
    func=search.run
)

import time
import pandas as pd

QUIZ_FILE = 'quiz2.csv'
OUTPUT_FILE = 'answered.csv'
FIELDS = ['id', 'question', 'y']

index = 0
START = 0
LENGTH = 220

if __name__ == "__main__":
    file = pd.read_csv(QUIZ_FILE, index_col='id', dtype='str')
    responses = []
    
    with open("google_searches_2.txt", "a") as f:
        for i, question in file.iterrows():
            if i >= START and i < START + LENGTH:
                try:
                    print(f"Getting answer to question {i}... ")
                    q = str(question['question']).split("\nOptions:")[0]
                    response = tool.run(q)
                    time.sleep(0.7)
                    f.write(''.join([c for c in response if c.isascii()]) + "\n\n")
                except Exception as e:
                    print(e)
                    break
            elif i >= START + LENGTH:
                break
            index += 1