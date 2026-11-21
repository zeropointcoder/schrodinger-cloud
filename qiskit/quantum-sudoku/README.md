# Quantum Sudoku Solver

Quantum Sudoku-style solver using Grover amplification with ancilla-based oracle for reliably marking multiple valid states.


## Overview
- Initialise `4` main qubits in superposition.

- Use 2 `ancilla` qubits to compute a single `is valid`? for all 4 valid `4`-qubit states.

- Apply a `phase flip` on the combined ancilla to `mark` valid states.

- Apply `Grover` diffusion to `amplify` probabilities of marked states.

- Measure the 4 main qubits to retrieve the `valid` Sudoku assignments.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_sudoku.py
```