# Shors Algorithm 8-qubit

Quantum implementation of Shor’s algorithm on a simulator to factor small integers (demonstration for N=15).


## Overview
- Prepare counting qubits in superposition and work qubits for modular exponentiation.

- Apply controlled modular exponentiation specific to `N=15`.

- Perform inverse Quantum Fourier Transform on counting qubits.

- Measure counting qubits to extract periodicity.

- Use measurement statistics to estimate factors of the target integer using simple `GCD` checks.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 shors_algorithm_8q.py
```