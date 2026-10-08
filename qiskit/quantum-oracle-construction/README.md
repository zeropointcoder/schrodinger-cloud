# Quantum Oracle Construction

Implement a reusable and modular quantum oracle construction for integration into larger quantum algorithms.

## Overview
- Match the target state: Add `X` gates to flip qubits where the marked state has a `0`, so the target becomes `|11…1⟩`.
- Apply a phase flip: Use a multi-controlled `Z` (implemented as `H–MCX–H`) to add a `−1` phase to that matched state only.
- Uncompute the mapping: Undo the earlier `X` gates so the circuit returns to the original basis.
- **Result**: Only the chosen computational basis state acquires a phase inversion, which is exactly what a quantum oracle must do.

## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_oracle_construction.py
```