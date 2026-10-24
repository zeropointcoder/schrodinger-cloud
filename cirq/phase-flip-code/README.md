# Phase Flip Code

`Phase-flip` quantum error correction using a `three-qubit` code example that protects a qubit against `phase errors`.


## Overview
- A `phase-flip` error corresponds to a `Pauli-Z` operation.
- Applying `Hadamard` gates maps `phase errors` ↔ `bit errors`:
    `𝐻𝑍𝐻=𝑋`

- The circuit:
    - Encodes `one` logical qubit across `three` physical qubits
    - Converts `phase` errors into detectable `bit` errors
    - Decodes and recovers the original state

- Majority voting ensures a single phase error does not corrupt the logical qubit.

- Measurement results are returned as bitstring counts, suitable for histogram plotting.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 phase_flip_code.py
```