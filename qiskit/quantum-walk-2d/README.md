# Quantum Walk 2D

A simple 2D quantum random walk demonstrating superposition and conditional shifts.


## Overview
- Initialise `2 qubits` in the `|0⟩` state.
- Apply `Hadamard` gates as a quantum "coin" to create superposition:
    `H|0⟩ = (|0⟩ + |1⟩)/√2`
- Apply conditional shift operations `(CNOTs)` for `2D` movement.
- Repeat steps as required.
- Measure qubits and collect counts, showing probability distribution of the walk.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_walk_2d.py
```