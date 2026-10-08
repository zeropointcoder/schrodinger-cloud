# XOR Circuit Learning

A trainable quantum circuit that learns the XOR function and outputs predicted probabilities.


## Overview
- Inputs `(x1, x2)` are encoded using `X` gates on qubits `0` and `1`.

- Variational `single-qubit` rotations `(RX, RY, RZ)` introduce `4` trainable parameters.

- Entanglement is added via `CNOTs` to encode `XOR` correlations.

- The `last` qubit is measured in the `Z-basis`; the probability of `1` approximates `XOR`.

- Parameters are optimised via finite-difference gradient descent to minimise `MSE`.

- Output is the predicted probability of `1` for all `4` XOR inputs.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 xor_circuit_learning.py
```