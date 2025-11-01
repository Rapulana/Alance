def analyze_counts(counts: dict):
    """Simple post-processing of measurement results."""
    total = sum(counts.values())
    probs = {k: v / total for k, v in counts.items()}
    return probs