# 🚀 AI Startup Pitch Evaluator

An AI-powered system that analyzes startup pitch decks and evaluates their investment readiness using Retrieval-Augmented Generation (RAG) and LLM reasoning.

---

## 🔍 Project Objective

Automatically extract insights from startup pitch decks and generate:

- Executive Summary
- Market Opportunity Analysis
- Business Model Evaluation
- Competitive Landscape Review
- Risk Assessment
- Investor Readiness Score (0–100)
- AI-generated Strategic Recommendations

---

## 🏗 System Architecture

User Upload → PDF Parsing → Slide Chunking → Embeddings → Vector Database → RAG Retrieval → Evaluation Modules → Scoring Engine → Structured Report

---

## 🧠 Core Technologies

- Python
- Streamlit
- LangChain
- Groq LLaMA 3.3 70B
- ChromaDB
- SentenceTransformers
- PyMuPDF

---

## 🔁 Retrieval-Augmented Generation (RAG)

Each evaluation module retrieves relevant pitch deck sections using semantic similarity search before invoking LLM reasoning.

This improves:
- Accuracy
- Explainability
- Context relevance
- Modular analysis

---

## 📊 Scoring Logic

Weighted scoring model:

| Module              | Weight |
|--------------------|--------|
| Market Opportunity | 25%    |
| Business Model     | 20%    |
| Competition        | 15%    |
| Risk Assessment    | 20%    |
| Traction Signals   | 20%    |

Final Score = Weighted Average × 10

---

## 🚀 How to Run

1. Clone repository
2. Create virtual environment
3. Install dependencies:
