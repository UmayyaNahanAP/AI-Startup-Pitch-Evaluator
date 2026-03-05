def analyze_market(rag_function, context):
    question = """
    Analyze TAM, SAM, SOM.
    Check if growth justification exists.
    Score market strength out of 10.
    """
    return rag_function(context, question)