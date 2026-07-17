# Quantum Basic Circuits

To create, simulate, and visualise a basic quantum circuit.


## Overview
- Initialise qubits and classical bits.

- Apply `Hadamard` gates → puts qubits in superposition.

- Apply `CNOT` chain → creates `GHZ`-like entanglement.

- Analyse: only `000..0` and `111..1` indicate `GHZ`-like state.


## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 quantum_basic_circuits.py
```

### Clone fix
```bash
### After cloning:

### 1. Create the shared environment for cirq, qiskit & hybrid apps
- `cd /Users/leo/dev/schrodinger-cloud`
- `python3 -m venv .venv`

### 2. Activate it
- `source /Users/leo/dev/schrodinger-cloud/.venv/bin/activate`
```

### Qiskit broken install fix
```bash
### If you see "invalid environment mixing Qiskit <1.0 and ≥1.0":

pip uninstall -y qiskit qiskit-terra qiskit-aer qiskit-ibmq-provider qiskit-ibm-provider
pip cache purge
pip3 install -r requirements.txt
```