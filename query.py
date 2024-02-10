# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
CLIENT = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

def answer_question(prompt: str) -> str:
    completion = CLIENT.chat.completions.create(
      model="local-model", # this field is currently unused
      messages=[
        #{"role": "system", "content": "Answer with single character (A, B, C) only (do not give description)"},
        {"role": "user", "content": prompt + "\nAnswer only with the option letter (A, B, C)."}
      ],
      temperature=0.1,
    )
    return completion.choices[0].message