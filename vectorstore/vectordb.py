import chromadb
from chromadb.config import Settings
from config.settings import CHROMA_DB_DIR

client = chromadb.Client(Settings(persist_directory=CHROMA_DB_DIR))
collection = client.get_or_create_collection("pitch_deck")

def store_embeddings(chunks, embeddings):
    for chunk, embedding in zip(chunks, embeddings):
        collection.add(
            documents=[chunk["text"]],
            embeddings=[embedding],
            ids=[str(chunk["id"])]
        )

def query_similar(query_embedding, n=5):
    return collection.query(
        query_embeddings=[query_embedding],
        n_results=n
    )