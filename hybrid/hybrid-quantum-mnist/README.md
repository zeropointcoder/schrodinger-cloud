# Hybrid Quantum MNIST

Hybrid quantum–classical neural pipeline combining Cirq-based feature encoding with a Qiskit variational circuit.


## Overview
- Classical image data `𝑥 ∈ 𝑅^𝑛` is reduced and encoded as rotation angles

- Cirq feature map applies
    `𝑅𝑥(𝜃𝑖) = 𝑒^(−𝑖𝜃𝑖𝑋/2)`

- Measurement averages act as classical features

- Qiskit variational layer applies:
    - Parameterised `𝑅𝑦(𝜃)` gates
    - Linear entanglement via `CNOT` chain

- Final measurements return bitstring counts:
    `𝑝(𝑧) = ∣⟨𝑧∣𝑈(𝜃)∣𝜓⟩∣^2`


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 hybrid_quantum_mnist.py
```