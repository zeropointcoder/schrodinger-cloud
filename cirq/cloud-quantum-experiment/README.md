# Cloud Quantum Experiment

A reusable framework to build, simulate, and analyse small entangled quantum circuits.


## Overview
- Initialise a quantum circuit with any number of qubits.

- Apply `single`-qubit and `two`-qubit gates (`Hadamard` and `CNOT`).

- Measure all qubits and simulate the circuit `multiple` times.

- Return and analyse measurement counts for `entanglement` verification.

- Optionally, generate a probability histogram for visualisation.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 cloud_quantum_experiment.py
```