# Error Corrected Teleportation

Error-corrected teleportation using 3-qubit bit-flip code and ancilla-based bit-flip error detection.


## Overview
- Encode qubit q0 using a `3-qubit` bit-flip repetition code

- Prepare entangled Bell pair between `q1` and `q2`

- Perform `Bell` measurement on `q0` and `q1`

- Apply `X` and `Z` corrections on `q2` based on measurement results

- Use `ancilla` qubits to detect `bit-flip` errors on `q2`


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 error_corrected_teleportation.py
```