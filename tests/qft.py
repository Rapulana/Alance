# tests/test_qft.py
from alance.algorithms import qft_circuit
from alance.executor import Executor

def test_qft_runs():
    qc = qft_circuit(n_qubits=3, measure=True)
    exe = Executor()
    out = exe.run(qc, shots=128)
    counts = out.get("counts", {})
    assert counts, "QFT returned no counts"
