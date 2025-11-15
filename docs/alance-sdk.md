---
id: alance-sdk
title: Alance SDK Overview
---

# Alance SDK — core components

- **Executor** — manages job submission, simulation or hardware execution.
- **Algorithms** — algorithm templates (VQE, QAOA, Grover, hybrid layers).
- **Visualize** — utilities to plot states, measure distributions.
- **Backends** — pluggable interfaces for simulators or hardware.

## How to extend
Add a new backend by implementing the `BaseBackend` interface (see `alance/backends/base.py` in the repo) and register it in the `Executor`.
