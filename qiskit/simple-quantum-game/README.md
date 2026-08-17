# Simple Quantum Game

An interactive single-qubit quantum game that lets players manipulate a real quantum state and win by steering measurement probabilities.


## Overview
- The player applies valid quantum gates (`X`, `H`, `Z`) to a `single` qubit

- The qubit state evolves according to quantum mechanics

- The circuit is measured over `many` shots for statistical validity

- The player `wins` by biasing the outcome towards `∣1⟩`

- Results are visualised and evaluated probabilistically


## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 simple_quantum_game.py
```