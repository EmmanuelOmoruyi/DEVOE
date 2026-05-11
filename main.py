from fastapi import FastAPI, UploadFile, File, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

import os

# =========================
# APP
# =========================

app = FastAPI()

# =========================
# PATHS
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# =========================
# STATIC FILES
# =========================

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static"
)

# =========================
# TEMPLATES
# =========================

templates = Jinja2Templates(
    directory=os.path.join(BASE_DIR, "templates")
)

# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# AI MODEL
# =========================

model = SentenceTransformer("all-MiniLM-L6-v2")

# =========================
# STORAGE
# =========================

chunks = []
chunk_vectors = []

k = 40

# =========================
# HOME PAGE
# =========================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

# =========================
# REQUEST MODEL
# =========================

class QueryRequest(BaseModel):
    query: str

# =========================
# COSINE SIMILARITY
# =========================

def cosine_similarity(a, b):

    dot = sum(float(x) * float(y) for x, y in zip(a, b))

    mag1 = sum(float(x) * float(x) for x in a) ** 0.5
    mag2 = sum(float(y) * float(y) for y in b) ** 0.5

    return dot / (mag1 * mag2 + 1e-8)

# =========================
# CHUNK CREATION
# =========================

def create_chunks(text):

    words = text.split()

    temp = []

    for i in range(0, len(words), k):

        chunk = words[i:i+k]

        temp.append(" ".join(chunk))

    return temp

# =========================
# RETRIEVAL
# =========================

def retrieve(query):

    global chunks
    global chunk_vectors

    print("ASK HIT")

    if len(chunks) == 0:

        return {
            "answer": "Upload a TXT file first.",
            "sources": []
        }

    query_vector = model.encode(query)

    results = []

    for i in range(len(chunks)):

        chunk_text = chunks[i]
        chunk_vector = chunk_vectors[i]

        score = cosine_similarity(
            query_vector,
            chunk_vector
        )

        results.append(
            (
                chunk_text,
                float(score)
            )
        )

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    top_3 = results[:3]

    top_chunks = [
        chunk for chunk, score in top_3
    ]

    answer = f"""
DEVOE Response

Question:
{query}

Most Relevant Context:
{top_chunks[0]}
"""

    return {

        "answer": answer,

        "sources": [

            {
                "text": chunk,
                "score": round(float(score), 3)
            }

            for chunk, score in top_3
        ]
    }

# =========================
# ASK ROUTE
# =========================

@app.post("/ask")
def ask(req: QueryRequest):

    return retrieve(req.query)

# =========================
# FILE UPLOAD
# =========================

@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    global chunks
    global chunk_vectors

    print("UPLOAD HIT")
    print("FILENAME:", file.filename)

    if not file.filename.endswith(".txt"):

        return {
            "message": "Only TXT files allowed."
        }

    contents = await file.read()

    try:

        text = contents.decode("utf-8")

    except:

        return {
            "message": "Could not decode TXT file."
        }

    chunks = create_chunks(text)

    print("CHUNKS CREATED:", len(chunks))

    chunk_vectors = model.encode(chunks)

    return {

        "message": "File uploaded successfully",

        "chunks_created": len(chunks)
    }