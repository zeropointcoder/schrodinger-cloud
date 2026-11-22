# BB84 Cryptography

Quantum key distribution using complementary measurement bases to establish a shared secret.


## Overview
- `Alice` encodes a random bit string using randomly chosen bases:
    - `Z` basis: `|0⟩`, `|1⟩`
    - `X` basis: `|+⟩ = (|0⟩ + |1⟩)/√2, |−⟩ = (|0⟩ − |1⟩)/√2`

- `Bob` measures each qubit using a randomly chosen basis

- Measurement outcomes only correlate when bases match

- Public comparison of bases allows discarding mismatches

- Remaining bits form the shared `secret key`


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 bb84_cryptography.py
```