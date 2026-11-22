# [CORE] Quantum Error Correction

Implements a complete quantum error-correction pipeline using logical encoding, noise, syndrome detection and recovery.


## Overview
- Logical Encoding
    - Logical qubit encoded as
        `∣0𝐿⟩ = ∣000⟩`, `∣1𝐿⟩ = ∣111⟩`

- Noise Injection
    - `Bit-flip` errors introduced using a `Pauli-X` noise channel

- Syndrome Extraction
    - `Ancilla` qubits detect parity violations without collapsing data

- Error Correction
    - `Conditional` recovery gates apply correction based on `syndrome`

- Decoding
    - Encoded qubit mapped back to `single-qubit` logical state

- Verification
    - Measurement confirms recovery despite `injected` noise


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_error_correction.py
```