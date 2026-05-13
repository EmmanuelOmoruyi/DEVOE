---
title: DEVOE
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
---

# DEVOE

A futuristic Retrieval-Augmented Generation (RAG) AI system built with FastAPI, Sentence Transformers, and a cyberpunk-inspired interface.

Supports:
- TXT files
- PDF files
- Semantic search
- Context retrieval
- Sci-fi UI


DEVOE — Local RAG Document Assistant

DEVOE is a futuristic Retrieval-Augmented Generation (RAG) web application built with FastAPI, JavaScript, and Sentence Transformers.

It allows users to:

Upload .txt documents
Convert documents into semantic chunks
Search document meaning using vector embeddings
Retrieve the most relevant context for a question
Interact through a futuristic cyberpunk UI
Features
Semantic document search
Vector similarity retrieval
FastAPI backend
Beautiful sci-fi/cyberpunk interface
Real-time chat UI
File upload system
Local embedding generation using Sentence Transformers
No paid API required
Tech Stack
Backend
Python
FastAPI
Sentence Transformers
Uvicorn
Frontend
HTML
CSS
JavaScript
AI / NLP
all-MiniLM-L6-v2 embedding model
Project Structure
DEVOE/
│
├── main.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
Installation
1. Clone Repository
git clone https://github.com/YOUR_USERNAME/DEVOE.git
cd DEVOE
2. Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Linux / Mac
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install fastapi uvicorn sentence-transformers python-multipart jinja2
Running DEVOE

Start the server:

uvicorn main:app --reload

Open browser:

http://127.0.0.1:8000
How DEVOE Works
Step 1 — Upload Document

DEVOE accepts .txt files.

The document is:

read
split into chunks
converted into vector embeddings
Step 2 — Ask Questions

User questions are converted into embeddings.

DEVOE compares:

question vector
against
document chunk vectors

using cosine similarity.

Step 3 — Retrieval

The most relevant chunks are returned as contextual answers.

Current Limitations

DEVOE currently performs:

semantic retrieval
contextual matching

but does NOT yet use an LLM for full answer generation.

This means:

answers are retrieved from document context
not fully AI-generated summaries

Future versions may integrate:

OpenAI
Ollama
Local LLMs
Streaming responses
Multi-document memory
PDF/DOCX support
Example
Uploaded Text
Batman is Bruce Wayne.
Superman is Clark Kent.
User Question
Who is Batman?
DEVOE Response
Batman is Bruce Wayne.
Future Roadmap
PDF support
DOCX support
Excel support
Ollama integration
OpenAI integration
Conversation memory
Vector database support
Multi-file retrieval
Better ranking algorithms
Streaming AI responses
UI Design

DEVOE uses a custom futuristic interface featuring:

neon glow effects
glassmorphism
cyberpunk aesthetics
animated borders
sci-fi inspired layout
Author

Built by Emmanuel Omoruyi

Project Name:
DEVOE — The Thinking Engine