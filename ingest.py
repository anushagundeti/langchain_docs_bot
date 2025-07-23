# ingest.py
import os
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

DATA_FILE = "data/example.txt"
DB_DIR = "faiss_index"

def ingest():
    loader = TextLoader(DATA_FILE)
    documents = loader.load()

    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(documents, embedding)
    db.save_local(DB_DIR)
    print("✅ FAISS vectorstore saved from text.")

if __name__ == "__main__":
    ingest()
