# Quantum GAN 2D

A hybrid quantum–classical GAN that learns a simple 2D probability distribution using quantum circuits.


## Overview
- Quantum Generator `(Qiskit)`
    - Uses a `2-qubit` variational circuit
    - Parameterised rotations:
        `𝑅𝑦(𝜃𝑥), 𝑅𝑦(𝜃𝑦)`
    - Entanglement via `CNOT`
    - Measurement produces a `2D` discrete distribution

- Quantum Discriminator `(Cirq)`
    - Independent quantum circuit evaluates generator samples
    - Applies bias rotation and entanglement
    - Scores likelihood of target state ∣11⟩

- `Hybrid` Loop
    - Qiskit generates samples
    - Cirq evaluates them
    - Classical optimisation can be added externally


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_gan.py
```