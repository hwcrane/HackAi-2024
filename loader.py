from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

_embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.load_local("faiss_index", _embeddings)
RETRIEVER = db.as_retriever(search_kwargs={"k": 1})


def get_relevant_info(question):
    docs = RETRIEVER.get_relevant_documents(question)
    return [doc.page_content for doc in docs]
