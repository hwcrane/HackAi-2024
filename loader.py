from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer, util

_embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
model = SentenceTransformer("all-MiniLM-L6-v2")
db = FAISS.load_local("faiss_index", _embeddings)
RETRIEVER = db.as_retriever()


def get_relevant_info(question):
    docs = RETRIEVER.get_relevant_documents(question)
    return [doc.page_content for doc in docs]

def deconstruct_question(question):
    asked, options = question.split("\nOptions:\n")
    a, b, c = [opt[3:]  for opt in options.split('\n')]
    return asked, a, b, c

def choose_closest(answer, a, b, c):
    target = model.encode(answer, convert_to_tensor=True)
    options = model.encode([a, b, c], convert_to_tensor=True)
    scores = util.cos_sim(target, options)
    closest = int(scores[0].argmax())

    if closest == 0:
        return 'A'
    elif closest == 1:
        return 'B'
    elif closest == 2:
        return 'C'
    
    print("THIS SHOULD NOT HAPPEN")
    
