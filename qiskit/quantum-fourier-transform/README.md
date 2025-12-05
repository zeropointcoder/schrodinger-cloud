# Quantum Fourier Transform

Implements the Quantum Fourier Transform on a quantum state.

## Overview
- **Initialisation**: Set up a quantum circuit with n qubits.
- **Hadamard Gates**: Apply Hadamard to each qubit to create superposition.
- **Controlled Phase Rotations**: Add controlled-phase gates between qubits with decreasing angles.
- **Qubit Reversal**: Swap qubits to reverse the order (standard in QFT).
- **Simulation**: Use AerSimulator to simulate the quantum circuit.
- **Visualisation**: Plot measurement results as a histogram.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 quantum_fourier_transform.py
```