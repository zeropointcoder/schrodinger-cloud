# Quantum Variational Classifier

A variational quantum classifier for simple datasets using parameterised circuits.


## Overview
- Construct a parameterised quantum circuit:
    - Apply rotations on each qubit:
        `𝑅𝑦(𝜃𝑖)∣0⟩ = cos⁡(𝜃𝑖/2)∣0⟩ + sin⁡(𝜃𝑖/2)∣1⟩`
    - Entangle qubits with `CZ` gates.

- Measure each qubit in the computational basis to extract counts.

- Use AerSimulator to execute the circuit and get measurement statistics.

- Variational parameters `(theta_i)` can be trained for classification tasks.

- Output is a count dictionary like `{'000': 512, '111': 512}` suitable for `plot_histogram`.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_variational_classifier.py
```