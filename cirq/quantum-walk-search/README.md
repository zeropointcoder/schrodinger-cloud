# Quantum Random Walk Search

Quantum random walk search using a `discrete coined walk` with a marked target state.


## Overview
- The walker position is encoded in qubits `∣x⟩`, with a separate coin qubit `∣c⟩`

- Initial state:
    `∣ψ0​⟩ = H^⊗n∣0⟩`

- Each step applies:
    - Coin operator: `C=H`
    - Conditional shift: `∣c⟩∣x⟩ → ∣c⟩∣x⊕c⟩`

- A marked position applies a phase flip:
    `∣xt​⟩ → −∣xt​⟩`

- Interference increases probability of measuring the marked state

- Final measurements return bitstring counts suitable for histogram plotting


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_random_walk_search.py
```