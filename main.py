# main.py
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# FastAPI setup
app = FastAPI()

# Request schema
class Query(BaseModel):
    question: str

# Load vectorstore
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

db = FAISS.load_local("faiss_index", embedding, allow_dangerous_deserialization=True)


# LLM using OpenRouter (OpenAI-compatible API)
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="mistralai/mistral-7b-instruct:free"
)

# RAG chain setup
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=True,
)

# Endpoint
@app.post("/ask")
async def ask(query: Query):
    result = qa_chain(query.question)
    return {
        "question": query.question,
        "answer": result["result"],
        "sources": [doc.metadata.get("source", "N/A") for doc in result["source_documents"]],
    }
