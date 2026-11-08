# Quantum RL

Implements and analyses a hybrid 2-qubit Bell states with fidelity computation.


## Overview
- Build a `2`-qubit quantum circuit with a `Hadamard` gate on the `first` qubit followed by a `CNOT` gate to `entangle` them.

- Measure the qubits on both `Qiskit` and `Cirq` simulators.

- Compute the state `fidelity` between the `simulated` state and the ideal `Bell` state.

- Visualise measurement outcomes with histograms and qubit states with `Bloch` spheres.

- Output the counts and fidelity metrics for comparison across simulators.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_rl.py
```