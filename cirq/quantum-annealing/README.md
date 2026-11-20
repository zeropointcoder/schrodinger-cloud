# Quantum Annealing

Simulates a simple quantum annealing process using Cirq and parameterised qubits.


## Overview
- Initialise `n` qubits in a line using Cirq.

- Add `Ising Hamiltonian` terms:
    `𝐻 = ∑𝑖<𝑗𝐽𝑖𝑗𝑍𝑖𝑍𝑗 + ∑𝑖ℎ𝑖𝑋𝑖`
    implemented with `CZ` gates and `rx` rotations.

- Apply a `transverse` field that decreases over time (`annealing` schedule) via `rx` rotations.

- Measure all qubits to get classical outcomes.

- Return bitstring counts from repeated simulation.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_annealing.py
```