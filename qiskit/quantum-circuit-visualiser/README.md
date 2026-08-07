# Quantum Circuit Visualiser

This project demonstrates the creation, simulation and visualisation of a quantum circuit


## Overview
- Initialise a `2`-qubit quantum circuit with `2` classical bits.

- Apply gates:
    - `Hadamard` on qubit `0` → creates superposition.
    - `CNOT` (0→1) → entangles qubit `0` and `1` to form a `Bell state`.

- Measure both qubits into classical bits.

- Print the circuit, show measurement counts, and plot a histogram.


## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 quantum_circuit_visualiser.py
```