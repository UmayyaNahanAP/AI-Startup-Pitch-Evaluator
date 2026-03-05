def analyze_competition(rag_function, context):
    question = """
    Identify competitors.
    Evaluate differentiation.
    Score competitive strength out of 10.
    """
    return rag_function(context, question)