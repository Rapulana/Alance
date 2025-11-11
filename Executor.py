from typing import Dict, Any
from qiskit import transpile, execute
from qiskit.providers.aer import AerSimulator

class Executor:
    """Executes QuantumCircuit on a selected backend (default: AerSimulator)."""

    def __init__(self, backend_name: str = "aer_simulator"):
        self.backend_name = backend_name
        try:
            self.backend = AerSimulator()
        except Exception as e:
            raise RuntimeError(f"AerSimulator unavailable: {e}")

    def run(self, circuit, shots: int = 1024) -> Dict[str, Any]:
        if circuit is None:
            raise ValueError("No circuit provided to Executor.run()")
        try:
            compiled = transpile(circuit, self.backend)
            job = execute(compiled, backend=self.backend, shots=shots)
            result = job.result()
            counts = result.get_counts()
            return {"counts": counts}
        except Exception as e:
            raise RuntimeError(f"Execution failed: {e}")
