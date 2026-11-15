# Teleportation with Error Correction

Quantum teleportation circuit with basic error correction and measurement outputs.


## Overview
- Prepare qubit `0` in the state to be teleported (e.g., `H` + `X` gates).

- Create a `Bell pair` between qubits `1` and `2` (`H` + `CX`) for entanglement.

- Encode qubit `0` onto qubit `1` using `CX` + `H`.

- Measure qubits `0` and `1` into a `2-bit` classical register.

- Apply classical corrections on qubit `2` using `if_test` blocks:  
    - If classical bits = `01` → apply `X` gate on qubit `2`  
    - If classical bits = `10` → apply `Z` gate on qubit `2`  
    - If classical bits = `11` → apply `X` + `Z` gates on qubit `2`

- Result: qubit `2` now contains the teleported state, matching the original state of qubit `0`.

- Output: measurement counts show all possible outcomes; qubit `2`’s state is corrected according to classical measurement.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 teleportation_error_correction.py
```