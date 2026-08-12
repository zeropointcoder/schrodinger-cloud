# Quantum Circuit Optimiser

Demonstrates quantum circuit optimisation by removing redundant gates and comparing gate counts.


## Overview
- Initialise the class with number of qubits and optimisation level.

- Build circuit with redundant gates for demonstration.

- Optimise circuit with `optimization_level=3`.

- Run simulation to obtain measurement counts.

- Print circuits, measurement counts, and plot histogram.

- Compare gate counts before and after optimisation to show the effect.


## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 quantum_circuit_optimiser.py
```