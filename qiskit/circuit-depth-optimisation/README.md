# Circuit Depth Optimisation

Demonstrates a 3-qubit Deutsch-Jozsa algorithm with circuit optimisation, simulation, and comparison of measurement results.


## Overview
- Builds a `3`-qubit + `1` auxiliary qubit Deutsch-Jozsa circuit.

- Prepares superposition with `Hadamards` and initialises the auxiliary qubit in `|1⟩`.

- Implements a constant or balanced oracle using controlled gates.

- Applies Hadamards again to detect interference and measures input qubits.

- Optimises the circuit with Qiskit transpiler and runs both original and optimised versions.

- Plots histograms to reveal whether the function is constant or balanced.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 circuit_depth_optimisation.py
```