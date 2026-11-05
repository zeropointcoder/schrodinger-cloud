# Quantum Hamiltonian

Simulates Trotterised evolution of a 2-qubit Hamiltonian with pre-rotations and calculates evolving expectation values.


## Overview
- Initialise qubits with small rotations to move away from `|00>`.
- Build a Trotterised `ZZ` Hamiltonian circuit (`CX-RZ-CX` repeated).
- Compute `<Z0>`, `<Z1>`, and `<Z0Z1>` expectation values after evolution.
- Return dynamic results showing Hamiltonian-induced correlations.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_hamiltonian.py
```