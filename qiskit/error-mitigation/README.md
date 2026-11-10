# Error Mitigation via Extrapolation

A 2-qubit parameterised Bell state experiment with measurement statistics and fidelity analysis.


## Overview
- Initialise a `2`-qubit parameterised quantum circuit.

- Prepare a `Bell` state and apply a variable `RZ` rotation.

- Measure qubits and collect counts over multiple shots.

- Sweep `θ` parameter to analyse changes in measurement outcomes.

- Calculate fidelity with ideal Bell state for each `θ`.

- Plot measurement probabilities and fidelity as a function of `θ`.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 error_mitigation.py
```