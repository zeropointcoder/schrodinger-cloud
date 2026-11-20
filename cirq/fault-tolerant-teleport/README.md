# Fault Tolerant Teleport

A quantum teleportation protocol using fault-tolerant encoding to protect qubit states.


## Overview
- Logical qubit encoding (bit-flip code)
    - Protects one qubit against single bit-flip errors using `3` physical qubits.
    - Formula: `|ψ⟩_logical = α|000⟩ + β|111⟩`

- Bell pair preparation
    - Standard entangled pair: `|Φ+⟩ = (|00⟩ + |11⟩)/√2`

- Teleportation
    - Apply `CNOT` between `logical qubit` and one half of `Bell pair`.
    - Apply `Hadamard` to logical qubit.
    - Measure the `two` qubits.
    - Apply `X` or `Z`corrections to remote qubit based on measurement.

- Fault-tolerance
    - Encoded qubit resists single `bit-flip` errors during teleportation.
    - Measurement and corrections are applied conditionally.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 fault_tolerant_teleport.py
```