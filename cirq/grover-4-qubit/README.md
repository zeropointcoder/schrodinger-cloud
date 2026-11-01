# Grover 4-Qubit

Grover’s algorithm implemented with Cirq `to locate` a `marked 4-qubit state`.


## Overview
- The system starts in an equal superposition:
	`∣𝜓⟩ = (1/sqrt(2^4)) * ∑∣𝑥⟩` (∑ is applied for x=0 to 15)

- The `oracle` flips the `phase` of the marked state
	`∣𝑥𝑡⟩ → −∣𝑥𝑡⟩`

- The `diffusion` operator performs `inversion` about the mean, `amplifying` the marked amplitude

- For `N = 16`, a `single` Grover iteration is sufficient:
    `k ≈ (π/4) * sqrt(N)`

- Measurement collapses the state, producing the target bitstring with `high` probability


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 grover_4_qubit_search.py
```