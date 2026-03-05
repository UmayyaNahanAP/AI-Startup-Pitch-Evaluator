def generate_report(summary):
    report = f"""
    ===== EXECUTIVE SUMMARY =====
    {summary['summary']}

    ===== MARKET ANALYSIS =====
    {summary['market']}

    ===== BUSINESS MODEL =====
    {summary['business']}

    ===== COMPETITION =====
    {summary['competition']}

    ===== RISK REPORT =====
    {summary['risk']}

    FINAL INVESTOR READINESS SCORE: {summary['final_score']}/100
    """
    return report