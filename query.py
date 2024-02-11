# Example: reuse your existing OpenAI setup
from openai import OpenAI
from loader import choose_closest, deconstruct_question, get_relevant_info

# Point to the local server
CLIENT = OpenAI(base_url='http://localhost:1234/v1', api_key='not-needed')
SUFFIX = (
    'Answer with single character (A, B, C, D, E, Z) only (do not give description)'
)
# CONTEXT_FLAG = 'You are in an aeronautics exam and this is one of the questions. You can Answer the question based only on the following context:'

CONTEXT_PREFIX = '### CONTENT:'
QUESTION_PREFIX = '### QUESTION:'


def answer_question(question: str) -> str:
    relevant_info = '\n'.join(get_relevant_info(question)[::-1])

    history = [
        {
            'role': 'system',
            'content': f'You are about to take an exam based on this text, can you make some notes: \n {relevant_info}',
        },
        {'role': 'user', 'content': relevant_info},
    ]
    completion = CLIENT.chat.completions.create(
        model='local-model',  # this field is currently unused
        messages=history,
        temperature=0.8,
        # max_tokens=50,
    )
    history.append(
        {'role': 'assistant', 'content': completion.choices[0].message.content}
    )
    history.append(
        {
            'role': 'user',
            'content': question +'\nZ. None of the above' + '\nAnswer with single character (A, B, C) only (do not give description)',
        },
    )
    history.append({'role': 'assistant', 'content': 'The answer is '})
    completion = CLIENT.chat.completions.create(
        model='local-model',  # this field is currently unused
        messages=history,
        temperature=0.1,
        max_tokens=10,
    )

    print(completion.choices[0].message.content)
    return completion.choices[0].message.content.strip()[0]
