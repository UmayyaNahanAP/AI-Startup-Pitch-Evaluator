from config.settings import WEIGHTS
import re

def extract_score(text):
    match = re.search(r'(\d+)/10', text)
    if match:
        return int(match.group(1))
    return 5

def compute_final_score(market, business, competition, risk):
    scores = {
        "market": extract_score(market),
        "business_model": extract_score(business),
        "competition": extract_score(competition),
        "risk": extract_score(risk),
        "traction": 7  # placeholder
    }

    final_score = sum(scores[k] * WEIGHTS[k] for k in WEIGHTS) * 10
    return round(final_score, 2)