import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# -----------------------------
# API KEYS
# -----------------------------
# GROQ API key for RAG pipeline
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

# -----------------------------
# EMBEDDING MODEL
# -----------------------------
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# -----------------------------
# VECTOR DATABASE
# -----------------------------
CHROMA_DB_DIR = "./chroma_db"

# -----------------------------
# EVALUATION WEIGHTS
# -----------------------------
WEIGHTS = {
    "market": 0.25,
    "business_model": 0.20,
    "competition": 0.15,
    "risk": 0.20,
    "traction": 0.20
}

