from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# loader = TextLoader("./documents/CFR/CFR-2023-title14-vol1.htm")
#
# documents = loader.load()
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# texts = text_splitter.split_documents(documents)
embeddings = HuggingFaceEmbeddings()
# db = FAISS.from_documents(texts, embeddings)

# FAISS.save_local(db, folder_path='faiss_index')
db = FAISS.load_local("faiss_index", embeddings)

retriever = db.as_retriever()

docs = retriever.get_relevant_documents("What type of microphone must be installed to meet the recording requirements of paragraph (a)(2) of 14 CFR 23.1457? ")
print(docs)

