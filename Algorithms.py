
from qiskit import QuantumCircuit

def bell_state():
    """
    Create and return a 2-qubit Bell state circuit (with measurements).
    """
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc

def teleportation_circuit():
    """
    Create and return a 3-qubit circuit implementing quantum teleportation.
    Qubit 0: state to teleport
    Qubit 1: Alice entanglement qubit
    Qubit 2: Bob entanglement qubit (target)
    """
    qc = QuantumCircuit(3, 2) 
    qc.h(0)
    qc.h(1)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])

    qc.x(2).c_if(qc.clbits[1], 1) 
    qc.z(2).c_if(qc.clbits[0], 1) 

    qc.barrier()
    qc.measure(2, 0) 
    return qc

def grover_search(n_qubits: int = 2, target: str = "11"):
    """
    Build a tiny Grover circuit searching for 'target' among 2^n_qubits elements.
    For v0.1 we implement a simple 2-qubit Grover that marks 'target'.
    Returns a circuit with measurements.
    """
    if n_qubits < 1:
        raise ValueError("n_qubits must be >= 1")
    if len(target) != n_qubits:
        raise ValueError("target bitstring length must equal n_qubits")

    qc = QuantumCircuit(n_qubits, n_qubits)

    for q in range(n_qubits):
        qc.h(q)

    for q, bit in enumerate(target):
        if bit == '0':
            qc.x(q)

    if n_qubits == 1:
        qc.z(0)
    elif n_qubits == 2:
        qc.h(1)
        qc.cx(0, 1)
        qc.h(1)
    else:
        pass

    for q, bit in enumerate(target):
        if bit == '0':
            qc.x(q)

    for q in range(n_qubits):
        qc.h(q)
        qc.x(q)
    
    if n_qubits == 2:
        qc.h(1)
        qc.cx(0,1)
        qc.h(1)
    else:
        pass
    for q in range(n_qubits):
        qc.x(q)
        qc.h(q)

    qc.measure(list(range(n_qubits)), list(range(n_qubits)))
    return qc
