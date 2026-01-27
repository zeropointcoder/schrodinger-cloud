# Phase Estimation 3 Qubits
`Phase Estimation` (PE) in quantum computing estimates the phase ϕ of an eigenvalue `e^2πiϕ` of a unitary operator `U`. In a Cirq implementation with 2-3 qubits, the algorithm uses a sequence of Hadamard gates and controlled-unitary operations to estimate this phase.

## Overview
1. **Prepare quantum registers**: Use `multiple` qubits for the `ancilla` register (to store the estimation) and `one` qubit for the state `whose phase` you want to estimate.

2. **Apply Hadamard gates** to the `ancilla` qubits to create superposition.

3. **Apply controlled-units** on each qubit, depending on the number of qubits used (e.g., U^{2^k}).

4. **Inverse Quantum Fourier Transform (QFT)** to collapse the state and obtain the phase.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 qpe_three_qubits.py
```