def analyze_business_model(rag_function, context):
    question = """
    Identify revenue streams.
    Evaluate pricing model.
    Detect missing business model components.
    Score out of 10.
    """
    return rag_function(context, question)