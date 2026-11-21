# Quantum Hubbard

A Hubbard model quantum simulation using Cirq.


## Overview
- Hubbard Model Hamiltonian:
    `𝐻 = −𝑡∑⟨𝑖,𝑗⟩,𝜎(𝑐𝑖𝜎†𝑐𝑗𝜎+ℎ.𝑐.) + 𝑈∑𝑖𝑛𝑖↑𝑛𝑖↓`
    - `​𝑡` = hopping term
    - `𝑈` = on-site interaction

- Circuit construction:
    - Use `XX+YY` gates for `hopping` between sites (simulates electron tunnelling)
    - Use `Z` rotation gates for on-site interaction
    - Measure all qubits to get occupation probabilities

- Simulation:
    - Cirq’s Simulator executes the circuit
    - Results converted to bitstring counts, representing electron configurations

- Run:
    - Prints circuit layout and counts from `500` repetitions.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_hubbard.py
```