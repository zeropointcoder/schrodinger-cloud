# Quantum Generative Model

A multi-qubit quantum generator that optimises a parameterised circuit to approximate a target probability distribution.


## Overview
- Initialise a parameterised quantum circuit with `n` qubits.

- Apply parameterised rotations and entanglement.

- Measure qubits to get counts and convert to probabilities.

- Define a cost function comparing generated and target distributions.

- Optimise parameters using a simple `gradient-free` method.

- Visualise the resulting probability distribution.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_generative_model.py
```