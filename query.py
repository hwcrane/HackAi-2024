# Example: reuse your existing OpenAI setup
from openai import OpenAI
from loader import get_relevant_info

# Point to the local server
CLIENT = OpenAI(base_url='http://localhost:1234/v1', api_key='not-needed')
SUFFIX = (
    'Answer with single character (A, B, C) only (do not give description)'
)
CONTEXT_FLAG = 'You are in an aeronautics exam and this is one of the questions. You can Answer the question based only on the following context:'


def answer_question(question: str) -> str:
    relevant_info = '\n'.join(get_relevant_info(question)[::-1])

    completion = CLIENT.chat.completions.create(
        model='local-model',  # this field is currently unused
        messages=[
            {"role": "system", "content": CONTEXT_FLAG + '\n' + relevant_info},
            {"role": "user", "content": question + "\n" + SUFFIX}
        ],
        temperature=0.3,
        max_tokens=10,
    )
    return completion.choices[0].message.content[0]
