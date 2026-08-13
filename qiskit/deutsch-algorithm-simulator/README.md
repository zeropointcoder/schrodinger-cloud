# Deutsch Algorithm Simulation

Implement Deutsch’s algorithm demonstrating how quantum interference distinguishes constant and balanced Boolean functions in a single query.


## Overview
- Prepares a `2`-qubit system with phase kickback

- Applies a configurable `oracle` (`constant` or `balanced`)

- Uses interference via `Hadamard` gates

- Measures the input qubit to classify the function


## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 deutsch_algorithm_simulator.py
```