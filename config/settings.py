import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
CHROMA_DB_DIR = "./chroma_db"

WEIGHTS = {
    "market": 0.25,
    "business_model": 0.20,
    "competition": 0.15,
    "risk": 0.20,
    "traction": 0.20
}