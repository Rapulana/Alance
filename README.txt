QuantStack: Lightweight Quantum Software Stack

QuantStack is an open-source framework for designing, compiling, executing,
and analyzing quantum algorithms.

Features
- Clean modular architecture
- Runs on Qiskit simulator backends
- Includes built-in Bell state example
- Docker-ready and testable

Example
'''python
from executor import Executor
from Algorithms import bell_state

executor  = Executor()
result = executor.run(bell_state())
print(result["counts"])