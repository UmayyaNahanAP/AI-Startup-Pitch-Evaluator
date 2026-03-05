def analyze_risk(rag_function, context):
    question = """
    Identify execution, financial, and market risks.
    Assign overall risk score out of 10 (higher = safer).
    """
    return rag_function(context, question)