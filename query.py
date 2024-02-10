# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
CLIENT = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
SUFFIX = ""

def answer_question(question: str, relevant_docs) -> str:
    

    completion = CLIENT.chat.completions.create(
      model="local-model", # this field is currently unused
      messages=[
        {"role": "system", "content": "Answer only with the option letter (A, B, C)."},
        {"role": "user", "content": PREFIX + "\n" + question + "\n" + SUFFIX}
      ],
      temperature=0.2,
    )
    return completion.choices[0].message