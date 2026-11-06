# Phase Estimation Molecules

Estimates `molecular energy phases` using quantum phase estimation.


## Overview
- A molecular Hamiltonian eigenvalue is encoded as a phase
    `𝑈∣𝜓⟩ = 𝑒^(2𝜋𝑖𝜑)∣𝜓⟩`

- `Control` qubits apply powers of the unitary operator to accumulate phase

- An `inverse Quantum Fourier Transform` extracts the binary phase estimate

- Measurement outcomes approximate
    `𝜑 ≈ ∑(𝑏𝑘/2^𝑘)` [∑ => 𝑘 = 1 to 𝑛]

- The most frequent bitstring corresponds to the molecular energy phase


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 phase_estimation_molecules.py
```