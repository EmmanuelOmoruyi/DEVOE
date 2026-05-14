---
title: DEVOE
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
---

# DEVOE

A futuristic Retrieval-Augmented Generation (RAG) system built with FastAPI, Sentence Transformers, and a cyberpunk-inspired interface.

DEVOE allows users to upload TXT and PDF documents, convert them into semantic embeddings, and retrieve relevant context using natural language questions.

---

## Features

- TXT file support
- PDF file support
- Semantic search
- Cosine similarity retrieval
- FastAPI backend
- Cyberpunk / futuristic interface
- Fully local AI pipeline
- No external APIs required
- Context-aware retrieval

---

## Demo Video

Click below to watch DEVOE in action:

🎥 [Watch Demo Video](./videos/devoe_screen_record.mp4)

---

## Screenshots

### Main Interface

[PLACE SCREENSHOT HERE]

### Retrieval Example

[PLACE SCREENSHOT HERE]

---

## How It Works

DEVOE follows a Retrieval-Augmented Generation workflow:

1. User uploads TXT or PDF documents  
2. Text is extracted from the document  
3. Text is split into chunks  
4. Sentence embeddings are generated  
5. User asks a question  
6. Query embeddings are generated  
7. Cosine similarity retrieves relevant chunks  
8. Most relevant context is returned

---

## Tech Stack

### Backend

- Python
- FastAPI
- Sentence Transformers
- PyPDF
- Uvicorn

### Frontend

- HTML
- CSS
- JavaScript

### AI/NLP

- all-MiniLM-L6-v2
- Semantic embeddings
- Cosine similarity retrieval

---

## Installation

Clone repository:

```bash
git clone https://github.com/EmmanuelOmoruyi/DEVOE.git
```

Enter directory:

```bash
cd DEVOE
```

Install requirements:

```bash
pip install -r requirements.txt
```

Run:

```bash
uvicorn main:app --reload
```

Open browser:

```bash
http://127.0.0.1:8000
```

---

## Project Structure

```bash
DEVOE/
│
├── main.py
├── requirements.txt
├── videos/
│   └── devoe_screen_record.mp4
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
└── README.md
```

---

## Example Workflow

### Upload

Upload TXT or PDF files

### Ask

Who is Batman?

### Response

DEVOE Response

Question:
Who is Batman?

Most Relevant Context:
Batman is Bruce Wayne.

---

## Deployment Status

DEVOE currently runs locally.

During deployment testing, multiple free cloud platforms were attempted. However, the embedding pipeline exceeded available free-tier memory limits due to PyTorch and Sentence Transformers requirements.

Rather than removing core retrieval functionality or replacing it with lower-quality alternatives, the project remains fully functional as a local deployment.

Future deployment goals:

- optimized inference pipeline
- lighter embedding models
- vector database integration
- optional LLM integration
- upgraded cloud infrastructure

---

## Future Improvements

- Persistent vector storage
- Chat memory
- Multi-document retrieval
- Better ranking system
- LLM-generated answers
- Authentication
- Docker deployment
- Streaming responses

---

## Author

Emmanuel Omoruyi

GitHub:

https://github.com/EmmanuelOmoruyi

---

## License

MIT License
