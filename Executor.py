# alance/executor.py
from typing import Dict, Any
from qiskit import transpile, execute
from qiskit.providers.aer import AerSimulator

class Executor:
    """
    Executes QuantumCircuit on selected backend.
    Default: AerSimulator for local runs.
    """

    def __init__(self, backend_name: str = "aer_simulator"):
        self.backend_name = backend_name
        try:
            # AerSimulator is used for local execution
            self.backend = AerSimulator()
        except Exception as e:
            # fallback: try default constructor, but raise if not available
            raise RuntimeError(f"AerSimulator initialization failed: {e}")

    def run(self, circuit, shots: int = 1024) -> Dict[str, Any]:
        """
        Transpile and execute circuit. Returns {"counts": {...}}.
        """
        if circuit is None:
            raise ValueError("No circuit provided to Executor.run()")

        try:
            compiled = transpile(circuit, self.backend)
            job = execute(compiled, backend=self.backend, shots=shots)
            result = job.result()
            counts = result.get_counts()
            return {"counts": counts}
        except Exception as e:
            # Provide actionable error message
            raise RuntimeError(f"Execution failed: {e}")
