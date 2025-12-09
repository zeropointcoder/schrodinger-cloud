# XOR Circuit Learning

Circuit Learning trains a parameterised quantum circuit to approximate a target function, like `XOR`, by optimising parameters based on measurement outcomes.

## Overview
- Initialise a parameterised quantum circuit with adjustable gates.
- Encode input data into quantum states using rotations.
- Apply multiple layers of trainable rotations and entanglement.
- Measure qubits to extract probabilities for prediction.
- Compute loss between predicted probabilities and target labels.
- Optimise parameters using a classical optimiser.
- Repeat until the circuit approximates the `XOR` function.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 xor_circuit_learning.py
```