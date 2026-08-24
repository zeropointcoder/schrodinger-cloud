# QAOA Maxcut Solver

QAOA-based MaxCut approximation on a small graph using Cirq.


## Overview
- Initialise all qubits in uniform superposition using `Hadamard` gates.

- Encode the `MaxCut` cost function using the `Ising Hamiltonian`:
    `H₍C₎ = Σ (1 − ZᵢZⱼ)/2` over graph edges.

- Apply alternating operators:
    - Cost unitary: `U(C, γ) = exp(−iγH₍C₎)`
    - Mixer unitary: `U(B, β) = exp(−iβΣXᵢ)`

- Measure in the computational basis.

- Aggregate bitstrings as counts to identify high-probability cut solutions.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 qaoa_maxcut_solver.py
```