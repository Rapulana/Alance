"""Alance package (extended)."""
from .core import Array, set_device, get_device
from .autodiff import Variable
from .quantum import Simulator, Qubit, H, X, CNOT, RX, RZ, measure

__all__ = [
    "Array", "set_device", "get_device",
    "Variable",
    "Simulator", "Qubit", "H", "X", "CNOT", "RX", "RZ", "measure"
]
