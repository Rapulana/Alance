"""
Alance: NumPy + Autodiff + Quantum simulator
Author: Pascal Rapulana
"""

from . import array
from . import core
from . import autodiff
from . import quantum

__all__ = [
    "array",
    "core",
    "autodiff",
    "quantum"
]

__version__ = "0.1.0"

def info():
    print("Alance version", __version__)
    print("Modules available:", __all__)
