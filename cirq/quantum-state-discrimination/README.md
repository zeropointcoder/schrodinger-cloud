# Quantum State Discrimination

Quantum state discrimination using a simple measurement basis change in Cirq.


## Overview
- Two possible quantum states are considered:
    - Computational basis state: `|0⟩`
    - Superposition state: `|+⟩ = (|0⟩ + |1⟩) / √2`

- Both states are passed through a `Hadamard` gate before measurement.

- Measurement is performed in the computational basis.

- The probability distributions differ:
    - H|0⟩ → |+⟩ → roughly equal 0/1 outcomes
    - H|+⟩ → |0⟩ → mostly 0 outcomes

- This asymmetry enables probabilistic state discrimination.

- Results are returned as classical bitstring counts suitable for histogram plotting.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_state_discrimination.py
```