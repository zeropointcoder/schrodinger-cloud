# Quantum Entanglement Measure

A quantum application that prepares a Bell state and measures `entanglement`.


## Overview
- Initialise a `2`-qubit quantum circuit.

- Apply `Hadamard` to qubit `0`, then `CNOT` to create a `Bell state`.

- Measure both qubits.

- Simulate measurements and collect counts.

- Visualise results with histogram and Bloch sphere for state inspection.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_entanglement_measure.py
```