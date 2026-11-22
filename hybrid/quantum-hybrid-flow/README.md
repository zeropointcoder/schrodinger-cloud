# Quantum Hybrid Flow

A hybrid quantum workflow estimating an angle using Cirq and applying it in a parameterised Qiskit circuit to analyse quantum measurement distributions.


## Overview
- Cirq circuit applies an `RX` rotation and measures a `single` qubit to estimate an `angle`.

- The estimated `angle` is used as a `parameter` in a `two`-qubit Qiskit circuit with `entanglement`.

- Qiskit circuit is simulated to produce measurement counts.

- Results are visualised and compared to validate the hybrid approach. 


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_hybrid_flow.py
```