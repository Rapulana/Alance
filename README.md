# Alance SDK

   
NumPy + Autodiff + Quantum Simulator — in one clean, lightweight Python SDK.

Alance is a minimal, hackable, open-source SDK that brings together:

Array computing (NumPy-like)

Automatic differentiation (PyTorch/JAX-style)

Quantum circuit simulation (Qiskit-style basics)

Optional GPU acceleration


Built for learning, experimentation, research, and building small ML/physics tools without heavy dependencies.



Features

- Alance Array

- NumPy-like API

- Supports Python lists, scalars

- Elementwise ops: + - * /

- Broadcasting

- Optional GPU support (via CuPy, if available)


# Reverse-Mode Autodiff

- Define variables, build expressions

- Compute gradients automatically

- Similar conceptual model to PyTorch but far simpler

- Perfect for building your own neural nets or optimizers


# Quantum Simulator

- Up to small 1–5 qubit states

- Common gates: H, X, Y, Z, CNOT, RX, RY, RZ

- Apply gates, simulate circuits, measure qubits

- Educational and extendable


 # Installation

- PyPI (recommended)

- pip install alance

- Local Development

- git clone https://github.com/<your-username>/Alance.git
cd Alance
pip install -e .


# Quick Start Demo (All Features in One)

from alance import Array, get_device, set_device
from alance.autodiff import Variable
from alance import Simulator, H, CNOT, RX

print("Device:", get_device())

# Arrays
a = Array([1, 2])
b = Array([3, 4])
print("a+b =", a + b)
print("a*b =", a * b)

# Autodiff
x, y = Variable(2.0), Variable(5.0)
z = x * y + x
z.backward()
print("z =", z.value)
print("dz/dx =", x.grad, "dz/dy =", y.grad)

# Quantum
sim = Simulator(2)
sim.apply_single_qubit_gate(H, 0)
sim.apply_cnot(0, 1)
sim.apply_param_gate(RX, 3.14159/2, 0)
print("State:", sim.state)
print("Measure qubit 0:", sim.measure(0))



# Project Structure

alance/
│
├── array.py          # NumPy-like Array class
├── autodiff/         # Reverse-mode autodiff engine
│   ├── variable.py
│   ├── functions.py
│
├── quantum/          # Quantum simulator + gates
│   ├── simulator.py
│   ├── gates.py
│
├── utils/            # Helper utilities
│
├── __init__.py
└── pyproject.toml    # Build configuration

A clean and simple architecture so you can read, understand, and extend everything.




# Architecture Diagram

┌─────────────────────┐
               │     Alance SDK      │
               └──────────┬──────────┘
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
┌────────────┐     ┌─────────────┐     ┌──────────────┐
│  Array      │     │  Autodiff   │     │  Quantum      │
│  (CPU/GPU)  │     │  Engine     │     │  Simulator    │
└────────────┘     └─────────────┘     └──────────────┘
       │                  │                  │
 ┌──────────┐      ┌────────────┐      ┌──────────────┐
 │ Ops: +-*  │      │ Graph-based│      │ H, X, CNOT    │
 │ shapes    │      │ derivatives│      │ RX, RY, RZ    │
 └──────────┘      └────────────┘      └──────────────┘



# Contributing

Contributions are welcome!

1. Fork the repo


2. Create a feature branch


3. Add tests if possible


4. Open a Pull Request



To run tests:

pytest .


# Roadmap

v0.2

- Vectorized math ops

- More quantum gates

- More autodiff functions (sin, cos, exp)

- Better GPU switching


v0.3

- Simple neural network module

- Quantum circuit builder API

- Sparse simulator option


v1.0

- Stable public API

- Documentation website

- Interactive notebooks



📄 License

This project is licensed under the MIT License (see LICENSE file).

