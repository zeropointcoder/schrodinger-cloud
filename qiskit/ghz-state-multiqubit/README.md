# GHZ State (Multi-Qubit)

Creates and measures a maximally entangled multi-qubit `Greenberger-Horne-Zeilinger` quantum state.


## Overview
- Initialise all qubits in the computational basis
    `∣000…0⟩`

- Apply a `Hadamard` gate to the `first` qubit
    `H∣0⟩= (​∣0⟩+∣1⟩)/√2`

- Cascade `CNOT` gates to `entangle` remaining qubits
    `(∣000…0⟩+∣111…1⟩​)/√2`

- Measure all qubits into classical registers

- Output bitstring counts suitable for `plot_histogram`


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 ghz_state_multiqubit.py
```