# Hybrid QCNN

This project implements a hybrid quantum-classical convolutional neural network (`QCNN`) using `TensorFlow Quantum` and `Qiskit`. 

- The hybrid workflow runs on **Linux x86_64 with Python 3.8–3.9**.
- On unsupported platforms (macOS, Windows, newer Python versions), only the **Qiskit verification circuit executes** safely.


## Overview
- Quantum convolution layer
    - Parameterised rotations: `𝑅𝑥(𝜃𝑖)`
    - Local entanglement using `CNOT` gates

- TensorFlow Quantum
    - Uses expectation values: `⟨Z⟩`
    - Optimised via classical gradient descent

- Hybrid workflow
    - `TFQ` handles training and optimisation
    - `Qiskit Aer` verifies quantum behaviour independently

- Measurement
    - Classical bitstrings returned as counts suitable for visualisation


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 hybrid_qcnn.py
```