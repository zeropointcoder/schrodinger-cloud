# Quantum Spin Chain (6-qubit)

Simulates a `6-qubit` spin chain with simple `CZ` interactions and measurements.


## Overview
- Initialise each qubit in a superposition:
    `∣+⟩ = (∣0⟩ + ∣1⟩)/sqrt(2)`

- Apply spin-chain interactions with `controlled-Z` gates (parameterised by `θ`):
    `𝑈𝐶𝑍𝜃 = exp⁡(−𝑖(𝜃/2)𝑍𝑖𝑍𝑖+1)`

- Measure all qubits to obtain classical bitstrings.

- Simulation counts show the probability distribution over possible states.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_spin_chain.py
```