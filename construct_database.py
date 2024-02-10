from langchain_community.document_loaders import (
    PyPDFDirectoryLoader,
)
# from langchain_experimental.text_splitter import SemanticChunker 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

### LOAD Documents

loader = PyPDFDirectoryLoader('documents/')
documents = loader.load()

### Embeddings

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

### Split Documents

text_splitter = RecursiveCharacterTextSplitter()
texts = text_splitter.split_documents(documents)

### Create Vector Database

db = FAISS.from_documents(texts, embeddings)
db.save_local('faiss_index')

### Testing

# retriever = db.as_retriever()
# print(retriever.get_relevant_documents("What type of microphone must be installed to meet the recording requirements of paragraph (a)(2) of 14 CFR 23.1457"))

