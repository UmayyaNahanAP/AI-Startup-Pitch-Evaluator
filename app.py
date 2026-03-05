import streamlit as st
import tempfile

from ingestion.pdf_parser import extract_text_from_pdf
from ingestion.chunker import chunk_slides
from embeddings.embedder import generate_embeddings
from vectorstore.vectordb import store_embeddings
from rag.rag_pipeline import run_rag
from evaluators.market_analyzer import analyze_market
from evaluators.business_model_analyzer import analyze_business_model
from evaluators.competition_analyzer import analyze_competition
from evaluators.risk_assessor import analyze_risk
from evaluators.scoring_engine import compute_final_score
from reports.report_generator import generate_report

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(page_title="AI Startup Pitch Evaluator", layout="wide")

st.title("🚀 AI Startup Pitch Evaluator")
st.write("Upload a startup pitch deck and get an AI-powered investor readiness report.")


# ---------------------------------------------------
# PDF GENERATION FUNCTION (DEFINED FIRST)
# ---------------------------------------------------
def generate_pdf(report_text):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    doc = SimpleDocTemplate(temp_file.name, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph("Pitch Deck Evaluation Report", styles["Heading1"]))
    elements.append(Spacer(1, 0.3 * inch))

    for line in report_text.split("\n"):
        elements.append(Paragraph(line, styles["Normal"]))
        elements.append(Spacer(1, 0.2 * inch))

    doc.build(elements)
    return temp_file.name


# ---------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------
uploaded_file = st.file_uploader("📄 Upload Pitch Deck PDF", type=["pdf"])


# ---------------------------------------------------
# MAIN PROCESSING LOGIC
# ---------------------------------------------------
if uploaded_file:

    with st.spinner("Analyzing pitch deck... Please wait ⏳"):

        # Save uploaded file
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())

        # Extract and process
        slides = extract_text_from_pdf("temp.pdf")
        chunks = chunk_slides(slides)

        texts = [c["text"] for c in chunks]
        embeddings = generate_embeddings(texts)
        store_embeddings(chunks, embeddings)

        full_context = "\n".join(texts)

        # Run evaluators
        market = analyze_market(run_rag, full_context)
        business = analyze_business_model(run_rag, full_context)
        competition = analyze_competition(run_rag, full_context)
        risk = analyze_risk(run_rag, full_context)

        final_score = compute_final_score(market, business, competition, risk)

        summary = {
            "summary": run_rag(full_context, "Provide executive summary."),
            "market": market,
            "business": business,
            "competition": competition,
            "risk": risk,
            "final_score": final_score
        }

        report = generate_report(summary)

    st.success("✅ Evaluation Complete!")

    # ---------------------------------------------------
    # DISPLAY REPORT
    # ---------------------------------------------------
    st.subheader("📊 Evaluation Report")
    st.text_area("Generated Report", report, height=600)

    # ---------------------------------------------------
    # DOWNLOAD BUTTON (ONLY APPEARS AFTER REPORT READY)
    # ---------------------------------------------------
    if st.button("📥 Download Report as PDF"):
        pdf_path = generate_pdf(report)

        with open(pdf_path, "rb") as f:
            st.download_button(
                label="Click Here to Download",
                data=f,
                file_name="Pitch_Evaluation_Report.pdf",
                mime="application/pdf"
            )

else:
    st.info("👆 Please upload a Pitch Deck PDF to begin analysis.")