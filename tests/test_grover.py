from alance.algorithms import grover_search
from alance.executor import Executor

def test_grover_basic():
    qc = grover_search(n_qubits=2, target="11")
    exe = Executor()
    out = exe.run(qc, shots=256)
    counts = out.get("counts", {})
    assert counts, "Grover produced no counts"
    
    assert any(k == "11" for k in counts.keys())
