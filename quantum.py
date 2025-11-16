"""Enhanced minimal quantum simulator with parameterized gates and optional device support."""
import numpy as np
from math import cos, sin
from .core import get_device, set_device

# Basic gates
X = np.array([[0,1],[1,0]], dtype=complex)
H = (1/np.sqrt(2)) * np.array([[1,1],[1,-1]], dtype=complex)

def RX(theta):
    return np.array([[cos(theta/2), -1j*sin(theta/2)],
                     [-1j*sin(theta/2), cos(theta/2)]], dtype=complex)

def RZ(theta):
    return np.array([[np.exp(-1j*theta/2), 0],
                     [0, np.exp(1j*theta/2)]], dtype=complex)

CNOT = np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,0,1],
    [0,0,1,0]
], dtype=complex)

def _kron_n(*mats):
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out

class Qubit:
    def __init__(self, index):
        self.index = index

class Simulator:
    def __init__(self, n_qubits):
        self.n = n_qubits
        self.state = np.zeros((2**n_qubits,), dtype=complex)
        self.state[0] = 1.0

    def _apply_full_operator(self, op, target):
        ops = []
        for i in range(self.n):
            ops.append(op if i == target else np.eye(2, dtype=complex))
        full = _kron_n(*ops[::-1])
        self.state = full @ self.state

    def apply_single_qubit_gate(self, gate, target):
        self._apply_full_operator(gate, target)

    def apply_param_gate(self, gate_fn, theta, target):
        gate = gate_fn(theta)
        self.apply_single_qubit_gate(gate, target)

    def apply_cnot(self, control, target):
        if self.n == 2 and {control, target} == {0,1}:
            self.state = CNOT @ self.state
            return
        new_state = np.copy(self.state)
        for i in range(len(self.state)):
            bits = [(i >> j) & 1 for j in range(self.n)]
            if bits[control] == 1 and bits[target] == 0:
                j = i | (1 << target)
                new_state[j] = self.state[i]
                new_state[i] = self.state[j]
        self.state = new_state

    def measure(self, qubit_index):
        probs = np.abs(self.state)**2
        zero_prob = sum(probs[i] for i in range(len(self.state)) if ((i>>qubit_index)&1)==0)
        r = np.random.random()
        result = 0 if r < zero_prob else 1
        new_state = np.copy(self.state)
        for i in range(len(self.state)):
            if ((i>>qubit_index)&1) != result:
                new_state[i] = 0
        norm = np.linalg.norm(new_state)
        if norm>0:
            new_state /= norm
        self.state = new_state
        return result

def measure(sim: Simulator, qubit: Qubit):
    return sim.measure(qubit.index)
