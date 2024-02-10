# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
CLIENT = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

def answer_question(prompt: str) -> str:
    completion = CLIENT.chat.completions.create(
      model="local-model",
      messages=[
        {"role": "system", "content": "Answer only with the option letter (A, B, C)."},
        {"role": "user", "content": prompt + "\nAnswer only with the option letter (A, B, C)."}
      ],
      temperature=0.1,
    )
    response = completion.choices[0].message.content
    print("Response: " + response)
    print("")
    return "A"