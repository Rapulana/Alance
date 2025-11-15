---
id: examples
title: Examples
---

# Examples

Below a minimal Bell state example using the Alance simulator API:

```python
# examples/bell_state.py
from alance import Executor, Circuit

# create a 2-qubit bell circuit
c = Circuit(2)
c.h(0)
c.cx(0,1)
c.measure_all()

exec = Executor(backend='simulator')
result = exec.run(c, shots=1024)
print("Counts:", result.counts)
