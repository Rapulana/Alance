"""Core array wrapper with optional GPU backend (numpy / cupy)."""
import importlib
import numpy as np

_DEVICE = "numpy"
_xp = np

def set_device(device_name: str):
    """Set backend device: 'numpy' or 'cupy' (if installed)."""
    global _DEVICE, _xp
    if device_name == "cupy":
        try:
            cp = importlib.import_module("cupy")
            _xp = cp
            _DEVICE = "cupy"
        except Exception:
            raise RuntimeError("cupy not available; install cupy or use numpy")
    else:
        _xp = np
        _DEVICE = "numpy"

def get_device():
    return _DEVICE

class Array:
    """Tiny wrapper around numpy/cupy arrays."""
    def __init__(self, data):
        if isinstance(data, Array):
            self._arr = data._arr
        else:
            self._arr = _xp.array(data)

    @property
    def shape(self):
        return self._arr.shape

    def astype(self, dtype):
        return Array(self._arr.astype(dtype))

    def to_numpy(self):
        # convert to CPU numpy array
        if _DEVICE == "cupy":
            return _xp.asnumpy(self._arr)
        return self._arr

    def __add__(self, other):
        if isinstance(other, Array):
            other = other._arr
        return Array(self._arr + other)

    def __mul__(self, other):
        if isinstance(other, Array):
            other = other._arr
        return Array(self._arr * other)

    def __repr__(self):
        return f"Array({self.to_numpy()!r})"
