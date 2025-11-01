from qiskit import Aer, transpile, execute
class Executor:
    """Executes quantum circuits on the chosen backend."""
    def __init__(self,
                 backend_type="aer_simulator"):
        try:
            self.backend = Aer.get_backend(backend_type)
        except Exception:
            self.backend = Aer.get_backend("aer_simulator")
            def run(self, circuit, shots=1024):
                compiled = transpile(circuit, self.backend)
                job = execute(compiled, backend=self.backend, shots=shots)
                result = job.result()
                counts = result.get_counts()
                return {"counts": counts}