# [HARDWARE / COMPILER] Quantum Transpiler Optimisation Pass

Optimises quantum circuits using single-qubit gate merging and advanced transpiler passes, then simulates the circuit.


## Overview
- Build a quantum circuit with:
    - `Hadamard` layer for superposition.
    - `CNOT` layer for entanglement.
    - Parameterised `Rz` rotations for flexibility.
    - Measurement of all qubits.

- Transpiler optimisation:
  - Merge consecutive `single-qubit` gates (`merge_single_qubit_gates_to_phased_x_and_z`)
  - Drop empty moments (`drop_empty_moments`)
  - Eject phased `Pauli` gates (`eject_phased_paulis`) and `Z` rotations (`eject_z`)

- Simulate using `cirq.Simulator` and obtain counts of bitstrings.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_transpiler_optimisation.py
```