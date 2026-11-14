# Quantum NLP

A hybrid quantum text processing pipeline combining Cirq-based encoding with Qiskit-based quantum transformation.


## Overview
- Text encoding
    - Characters are mapped to integers using Unicode values
    - A rotation angle is computed:
        - `θ = (Σ char codes mod 360) · π / 180`

- Cirq quantum feature extraction
    - Single-qubit rotation: `Ry(θ)`
    - Measurement frequency produces a classical feature:
        - `𝑓 = 𝑃(∣1⟩)`

- Qiskit quantum transformation
    - Feature controls a parameterised `Ry` gate
    - Entanglement via `CNOT`
    - Measurement produces bitstring counts:
        - {00, 01, 10, 11}

- Hybrid flow
    - Cirq → classical feature → Qiskit
    - Fully compatible with `plot_histogram(counts)`


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_nlp.py
```