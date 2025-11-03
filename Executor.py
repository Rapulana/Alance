from typing import Dict, Any
from qiskit import transpile, execute
from qiskit.providers.aer import AerSimulator

class Executor:
    """Executes QuantumCircuit on a chosen backend (default: AerSimulator)."""

    def __init__(self, backend_name: str = "aer_simulator"):
        
        try:
            self.backend = AerSimulator()
        except Exception as e:
            
            self.backend = AerSimulator()

    def run(self, circuit, shots: int = 1024) -> Dict[str, Any]:
        """
        Transpile and execute the provided QuantumCircuit.
        Returns a dict: {"counts": {...}}
        """
        compiled = transpile(circuit, self.backend)
        job = execute(compiled, backend=self.backend, shots=shots)
        result = job.result()
        counts = result.get_counts()
        return {"counts": counts}
