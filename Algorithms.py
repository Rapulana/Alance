from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

def bell_state():
    """
    2-qubit Bell state (measured).
    """
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc

def teleportation_circuit():
    """
    3-qubit teleportation circuit with measurements.
    We prepare a simple |+> on qubit 0 to teleport.
    """
    qc = QuantumCircuit(3, 3)
    qc.h(0)

    qc.h(1)
    qc.cx(1, 2)

    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])

    qc.barrier()
    qc.measure(2, 2)
    return qc

def grover_search(n_qubits: int = 2, target: str = "11"):
    """
    Small Grover's algorithm for n_qubits (v1 supports n_qubits=2).
    Marks 'target' string.
    Returns a QuantumCircuit with measurements.
    """
    if n_qubits < 1:
        raise ValueError("n_qubits must be >= 1")
    if len(target) != n_qubits:
        raise ValueError("target bitstring length must equal n_qubits")

    qc = QuantumCircuit(n_qubits, n_qubits)

    qc.h(range(n_qubits))

    for i, bit in enumerate(target):
        if bit == '0':
            qc.x(i)
            
    if n_qubits == 1:
        qc.z(0)
    elif n_qubits == 2:
        qc.h(1)
        qc.cx(0, 1)
        qc.h(1)
    else:
        pass

    for i, bit in enumerate(target):
        if bit == '0':
            qc.x(i)

    for i in range(n_qubits):
        qc.h(i)
        qc.x(i)

    if n_qubits == 1:
        qc.z(0)
    elif n_qubits == 2:
        qc.h(1)
        qc.cx(0, 1)
        qc.h(1)
    else:
        pass

    for i in range(n_qubits):
        qc.x(i)
        qc.h(i)

    qc.measure(range(n_qubits), range(n_qubits))
    return qc

def qft_circuit(n_qubits: int = 3, measure: bool = True):
    """
    Quantum Fourier Transform (QFT) for n_qubits.
    Returns a circuit; measures if measure=True.
    """
    qc = QuantumCircuit(n_qubits, n_qubits if measure else 0)
    qft = QFT(num_qubits=n_qubits, do_swaps=True).decompose()
    qc.append(qft, range(n_qubits))
    if measure:
        qc.measure(range(n_qubits), range(n_qubits))
    return qc

