# Quantum State Tomography

`Quantum state tomography` using measurements in the `X`, `Y` and `Z` bases.


## Overview
- A quantum state `|ψ⟩` is prepared using a `Hadamard` gate

    `∣ψ⟩ = (​∣0⟩+∣1⟩​)/√2`

- Measurements are performed in three complementary bases:
    - `Z` basis: `direct` measurement
    - `X` basis: apply `H` before measurement
    - `Y` basis: apply `S†` then `H` before measurement

- Each basis provides expectation values: `⟨σx​⟩`, `⟨σy​⟩`, `⟨σz​⟩`

- Combined statistics reconstruct the state’s `Bloch` vector components.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_state_tomography.py
```