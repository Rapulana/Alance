from typing import Dict

def analyze_counts(counts: Dict[str, int], precision: int = 3) -> Dict[str, float]:
    """
    Convert raw measurement counts to probabilities.
    """
    if not counts:
        return {}
    total = sum(counts.values())
    return {k: round(v / total, precision) for k, v in counts.items()}
