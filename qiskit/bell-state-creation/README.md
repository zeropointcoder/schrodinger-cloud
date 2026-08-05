# Bell State Creation

This project demonstrates the creation of a `Bell State` (specifically entangled state) 
$$
|\Psi^+\rangle = \frac{1}{\sqrt{2}} (|00\rangle + |11\rangle)
$$ 

The Bell state is created by applying a `Hadamard` gate on the first qubit followed by a `CNOT` gate between the first and second qubits.


## Overview
- Sets up a `2`-qubit quantum circuit and simulator.

- Applies `Hadamard` to qubit `0` and `CNOT` to entangle both qubits, then measures.

- Displays a histogram of measured outcomes.

- Returns the raw measurement counts as a dictionary.


## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 bell_state_creation.py
```