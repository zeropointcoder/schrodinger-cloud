# Combined Error Code

Implements a 3-qubit repetition code with simple error detection and correction under a simulated noisy environment.


## Overview
- Prepares a logical qubit in superposition.

- Encodes it across `3` physical qubits (repetition code).

- Introduces a `single`-qubit `bit-flip` error probabilistically.

- Detects the error using `syndrome` measurement.

- Corrects the error and measures the final logical qubit.

- Simulates noisy behaviour with a noise model.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 combined_error_code.py
```