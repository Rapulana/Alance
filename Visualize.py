# alance/visualize.py
from typing import Dict
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

def plot_counts(counts: Dict[str, int], title: str = "Measurement distribution"):
    """
    Simple wrapper that plots a histogram of counts.
    Returns the matplotlib figure.
    """
    fig = plot_histogram(counts)
    fig.suptitle(title)
    plt.show()
    return fig
