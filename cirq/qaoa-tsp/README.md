# QAOA TSP (Traveling Salesman Problem)

The algorithm prepares a quantum state where shorter routes acquire higher probability by alternating distance-based phase penalties and mixing rotations.


## Overview
- Problem setup
    - Takes a distance matrix between cities (`TSP-like problem`).
    - Uses a hybrid quantum-classical idea inspired by `QAOA`.

- Qubits
    - Each city is represented by `one` qubit.
    - All qubits start in a superposition using `Hadamard` gates.

- Cost Hamiltonian
    - Encodes distances between cities using `ZZ` interactions.
    - Larger distances apply stronger phase penalties.
    - Controlled by parameter `γ` (gamma).

- Mixer Hamiltonian
    - Applies `X-rotations` to all qubits.
    - Allows the system to explore different solutions.
    - Controlled by parameter `β` (beta).

- QAOA layers
    - Repeats cost + mixer steps `p` times (default = 1).

- Measurement
    - Measures all qubits to produce bitstrings.
    - Each bitstring represents a possible route encoding.

- Simulation
    - Runs the circuit multiple times (shots).
    - Counts how often each solution appears.

- Output
    - Prints the most frequent bitstrings (best candidates).
    - Displays the quantum circuit used.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 qaoa_tsp.py
```