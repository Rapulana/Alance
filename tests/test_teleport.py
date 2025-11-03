from alance.algorithms import teleportation_circuit
from alance.executor import Executor

def test_teleport_runs():
    qc = teleportation_circuit()
    exe = Executor()
    out = exe.run(qc, shots=128)
    counts = out.get("counts", {})
    assert counts, "Teleportation produced no counts"
