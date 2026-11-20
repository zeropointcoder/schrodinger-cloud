# Circuit Compression

A quantum circuit simulator with multi-parameter rotation and variational optimisation.


## Overview
- Build a linear chain quantum circuit with parameterised `RY` rotations and `CNOT` entanglement.

- Bind rotation parameters and simulate measurement outcomes.

- Compute a simple cost function (probability of all qubits being `|0⟩`).

- Optimise parameters to maximise the cost, illustrating a basic variational quantum algorithm.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 circuit_compression.py
```