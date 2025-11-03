from alance.algorithms import bell_state
from alance.executor import Executor
from alance.analyzer import analyze_counts

def test_bell_basic():
    qc = bell_state()
    exe = Executor()
    out = exe.run(qc, shots=256)
    counts = out.get("counts", {})
    assert counts, "No counts returned"
    
    keys = list(counts.keys())
    assert any(k in keys for k in ("00","11"))
    probs = analyze_counts(counts)
    assert probs, "No probabilities calculated"
