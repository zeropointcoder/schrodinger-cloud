# Quantum Pipeline

Quantum feature encoding with Cirq and a multi-qubit Qiskit model for measuring input-dependent expectation values.


## Overview
- Encode classical input values into qubit rotations using Cirq.

- Construct a multi-qubit entangled circuit in Qiskit.

- Apply parameterised rotations based on encoded values.

- Measure the circuit and compute expectation values to observe input-dependent behaviour.

- Repeat for multiple inputs to visualise how the quantum model responds.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_pipeline.py
```