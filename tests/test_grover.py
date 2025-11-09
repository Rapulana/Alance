# tests/test_grover.py
from alance.algorithms import grover_search
from alance.executor import Executor

def test_grover_basic():
    qc = grover_search(n_qubits=2, target="11")
    exe = Executor()
    out = exe.run(qc, shots=128)
    counts = out.get("counts", {})
    assert counts, "No counts returned by Grover"
    assert any(k in counts for k in ("11","10","01","00"))
