# 🧠 LangChain RAG Q&A App with FastAPI + OpenRouter + HuggingFace + FAISS

This is a simple but powerful **Question-Answering (Q&A)** application that uses:

- 🧠 LangChain for chaining LLMs and retrievers
- 🤖 OpenRouter (`mistral-7b-instruct`) as the LLM backend
- 📚 HuggingFace embeddings to embed documents
- 🔍 FAISS for fast vector search
- ⚡ FastAPI for exposing the `/ask` endpoint
- 📄 A `.txt` document as your knowledge base

---

## 🚀 What It Does

- Upload or modify a `.txt` file with your knowledge
- Ingest and index it using FAISS
- Ask questions via a simple POST API
- Get answers grounded in your own document (RAG: Retrieval-Augmented Generation)

---

## 📦 Prerequisites

- Python 3.10+
- A free [OpenRouter](https://openrouter.ai/) API key
- `pip` and virtual environment setup

---

## 🔧 Installation

```bash
git clone https://github.com/your-username/langchain-docs-bot.git
cd langchain-docs-bot

python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

pip install -r requirements.txt

## 🔑 Setup Environment

Create a `.env` file in the root directory:

```ini
OPENROUTER_API_KEY=your_openrouter_api_key_here

## 📝 Add Your Document
Place your .txt file inside the data/ folder:

You can write anything — this file is the "brain" for your chatbot.

## 📥 Commands to execute ingest file and start server

- python ingest.py
- uvicorn main:app --reload


### ✅ Test the API (Postman or curl)

POST http://localhost:8000/ask
Content-Type: application/json

{
  "question": "What is this document about?"
}

Response

{
  "question": "What is this document about?",
  "answer": "This document discusses artificial intelligence and machine learning.",
  "sources": ["N/A"]
}
