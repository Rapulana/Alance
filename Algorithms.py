from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

def bell_state():
    """2-qubit Bell state (with measurements)."""
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0,1], [0,1])
    return qc

def teleportation_circuit():
    """3-qubit teleportation demo (prepare |+> on qubit0)."""
    qc = QuantumCircuit(3, 3)
    qc.h(0) 
    qc.h(1)
    qc.cx(1, 2)   
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0,1], [0,1])
    qc.barrier()
    qc.measure(2, 2)
    return qc

def grover_search(n_qubits: int = 2, target: str = "11"):
    """Small Grover implementation (n_qubits=1 or 2 supported)."""
    if len(target) != n_qubits:
        raise ValueError("target length must match n_qubits")
    qc = QuantumCircuit(n_qubits, n_qubits)
    qc.h(range(n_qubits))
    
    for i, bit in enumerate(target):
        if bit == '0':
            qc.x(i)
    if n_qubits == 1:
        qc.z(0)
    elif n_qubits == 2:
        qc.h(1); qc.cx(0,1); qc.h(1)
    for i, bit in enumerate(target):
        if bit == '0':
            qc.x(i)
    for i in range(n_qubits):
        qc.h(i); qc.x(i)
    if n_qubits == 1:
        qc.z(0)
    elif n_qubits == 2:
        qc.h(1); qc.cx(0,1); qc.h(1)
    for i in range(n_qubits):
        qc.x(i); qc.h(i)
    qc.measure(range(n_qubits), range(n_qubits))
    return qc

def qft_circuit(n_qubits: int = 3, measure: bool = True):
    """QFT using Qiskit's library; measures if requested."""
    qc = QuantumCircuit(n_qubits, n_qubits if measure else 0)
    qft = QFT(num_qubits=n_qubits, do_swaps=True).decompose()
    qc.append(qft, range(n_qubits))
    if measure:
        qc.measure(range(n_qubits), range(n_qubits))
    return qc
