from Executor import Executor
from Algorithms import bell_state
def test_bell_state():
    executor = Executor()
    circuit = bell_state
    result = executor.run(circuit, shots=200)
    keys = list(result["counts"].keys())
    assert "00" in keys or "11" in keys