from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",   
    temperature=0
)

def run_rag(context, question):
    prompt = ChatPromptTemplate.from_template("""
You are a senior venture capital analyst.

Use the startup pitch deck context to answer.

Context:
{context}

Question:
{question}

Provide:
- Structured reasoning
- Clear explanation
- If scoring required, give score like 8/10
- Justify the score
""")

    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "question": question
    })

    return response.content



