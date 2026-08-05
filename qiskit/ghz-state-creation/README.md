# Greenberger-Horne-Zeilinger (GHZ) State Creation

This project demonstrates the creation of a `GHZ` state


## Overview
- Initialise circuit – `3` qubits, `3` classical bits.

- Create superposition – `Hadamard` gate on qubit `0`.

- Entangle qubits – `CNOT` gates link qubits `0→1→2`.

- Measure qubits – Store results in classical bits.

- Plot histogram of measurement outcomes.


## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 ghz_state_creation.py
```