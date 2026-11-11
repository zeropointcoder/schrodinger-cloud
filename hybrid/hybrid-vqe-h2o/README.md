# Hybrid VQE H2O

Hybrid VQE + Classical optimisation for H₂O molecule simulation.


## Overview
- Qiskit prepares a parameterised variational quantum circuit:
    - Single-qubit rotations: `𝑅𝑦(𝜃)`
    - Entanglement: `CX` gates

- Cirq prepares a simple entangled circuit with `H` + `CNOTs`

- Both circuits are measured to produce bitstring counts

- A classical optimiser (from `scipy.optimize`) is used to minimise an energy-like function

- The output is the bitstring counts for Qiskit and Cirq circuits

- Optional: Qiskit circuit can be visualised using `QuantumCircuit.draw()`


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 hybrid_vqe_h2o.py
```