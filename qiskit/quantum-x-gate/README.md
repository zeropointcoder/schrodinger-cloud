# Quantum NOT Gate (X-Gate)

Implement and simulate a Quantum NOT Gate (`Pauli-X` gate).

## Overview
- `3` qubits initialised (can be increased if desired).

- Qubit `0`: `Hadamard` gate puts it in superposition.

- `Other` qubits: `X` gate flips them to `|1⟩` deterministically.

- CNOT gate from qubit `0` to each other qubit, creating correlations.

- All qubits are measured, giving a histogram of outcomes that reflects the superposition and entanglement.


## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 quantum_x_gate.py
```