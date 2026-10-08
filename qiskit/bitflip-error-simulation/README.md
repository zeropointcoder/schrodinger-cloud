# Bit-Flip Error Simulation

To prepare a qubit in state `∣1⟩`, apply a classical `bit-flip` channel with probability `p`, and measure the outcome to estimate how often the error flips the bit.

## Overview
1. Noise Model: 
    - Qiskit `pauli_error` is used to create a `bit-flip` channel:
        - With probability `p` apply `X`
        - With probability `1 − p` apply identity

2. Simulation
    - Prepare the qubit in `∣1⟩`
    - Insert an `id` gate so the error model has an operation to attach to
    - Measure the qubit over many shots (e.g., `2000`)

3. Expected Outcome
    - Ideal (no error): always measure `1`
    - With `bit-flip` error: about `p × shots` outcomes become `0`

## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 bitflip_error_simulation.py
```