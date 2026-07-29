# Quantum AND Gate (Toffoli Gate)

To implement a quantum AND gate using the Toffoli (CCX) gate.


## Overview
- Initialise a `3`-qubit quantum circuit.

- Optionally set qubits `0` and `1` to `0` or `1` (classical inputs).

- If no input, put qubits in superposition using `Hadamard` gates.

- Apply a `Toffoli (CCX)` gate: qubit `2` becomes `1` only if both inputs are `1`.

- Measure qubit `2` to get the `AND` result.

- Plot histograms for all input combinations or superposition case.


## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 quantum_and_gate.py
```