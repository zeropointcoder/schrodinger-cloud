# Entanglement Entropy

Computes and verifies quantum entanglement using entropy and measurement statistics.


## Overview
- A `Bell state` is prepared using:
    - `Hadamard` gate: `𝐻∣0⟩ = (∣0⟩ + ∣1⟩)/sqrt(2)`
    - `Controlled-NOT` gate to entangle qubits.

- The full quantum state `𝜌` is reduced via a partial trace:
    `𝜌𝐴 = Tr𝐵(𝜌)`

- Entanglement is quantified using von Neumann entropy:
    `𝑆(𝜌𝐴) = −Tr(𝜌𝐴log⁡2𝜌𝐴)`

- Measurements are added only after entropy calculation to preserve the pure state.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 entanglement_entropy.py
```