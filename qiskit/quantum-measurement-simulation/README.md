# Quantum Measurement Simulation

Simulate **quantum measurement**.


## Overview
- Sets qubits, shots, rotation angle, and output folder.

- Build circuit:
    - Qubit `0` → superposition `(H)`
    - Qubit `0` → rotation `(RY)`
    - Qubits `0` & `1` → entanglement `(CNOT)`
    - All qubits → measurement

- Transpile the circuit and execute on simulator.

- Calculate and print probabilities of all outcomes.

- Save and display measurement results.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 quantum_measurement_simulation.py
```
