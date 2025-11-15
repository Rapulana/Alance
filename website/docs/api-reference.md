---
id: api-reference
title: API Reference
---

# API Reference

**Goal:** auto-generate this from source. Recommended approaches:
- If your core is Python: use **Sphinx** to generate HTML into `website/docs/api/` and link here.
  - Tools: Sphinx + autodoc + napoleon (+ breathe if you want Doxygen for C/C++).
- Or generate markdown from docstrings and copy into `docs/api`.

For now, this page documents the high-level modules:
- `alance.executor.Executor`: create, submit jobs.
- `alance.circuit.Circuit`: build circuits.
- `alance.backends`: available backends.
