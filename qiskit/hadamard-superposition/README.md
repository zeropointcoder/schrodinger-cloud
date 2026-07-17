# Hadamard single qubit superposition

Implement quantum superposition on a single qubit.


## Overview
- Create a `1`-qubit quantum circuit with `1` classical bit.

- Apply the `Hadamard` gate `(H)` → qubit is now in equal superposition of `|0⟩` and `|1⟩`.

- Apply a `phase` gate `(P)` → rotates qubit state on the `Bloch` sphere, shows phase effect.

- Use Bloch sphere to visualise qubit state `before` measurement.

- Measure qubit → collapses superposition to classical `0` or `1`.

- Run circuit on a simulator `multiple` times (shots) → `collect` statistics.

- Compare `theoretical` vs `simulated` probabilities and display as histogram.


## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 hadamard_superposition.py
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