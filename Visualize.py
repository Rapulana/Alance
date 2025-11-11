from qiskit.visualization import plot_histogram
from typing import Dict

def visualize_counts(counts: Dict[str, int], title: str = "Distribution"):
    """Return a matplotlib figure (caller may show/save it)."""
    fig = plot_histogram(counts)
    try:
        fig.suptitle(title)
    except Exception:
        pass
    return fig
