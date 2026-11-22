# [CORE] Custom QAOA Mixer

This project explores a problem-specific Quantum Approximate Optimisation Algorithm using a non-standard mixer `Hamiltonian`.


## Overview
- Initial State
    - Uniform superposition prepared using `Hadamard` gates:
        `∣𝜓0⟩ = 1/sqrt(2^𝑛) * ∑𝑥∣𝑥⟩`

- Cost Hamiltonian
    - Encodes `Max-Cut` using:
        `𝐻𝐶 = ∑(𝑖,𝑗)∈𝐸 (1−𝑍𝑖𝑍𝑗)/2`
    - Implemented via `CNOT–RZ–CNOT` constructions

- Custom Mixer Hamiltonian
    - Combines:
        - Local transverse field: `∑𝑖𝑋𝑖`
        - Entangling `XY`-style interactions:
            `𝐻𝑀 = ∑𝑖𝑋𝑖 + ∑𝑖(𝑋𝑖)(𝑋𝑖 + 1)`

- Variational Layers
    - Alternating application of:
        `𝑒^(−𝑖𝛾𝐻𝐶)` and `𝑒^(−𝑖𝛽𝐻𝑀​)`

- Measurement
    - Samples bitstrings corresponding to candidate solutions


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 custom_qaoa_mixer.py
```