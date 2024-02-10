from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

_embeddings = HuggingFaceEmbeddings()
db = FAISS.load_local("faiss_index", _embeddings)
RETRIEVER = db.as_retriever()

def get_relevant_info(question):
    docs = RETRIEVER.get_relevant_documents(question)
    return docs