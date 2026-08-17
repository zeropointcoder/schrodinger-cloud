# VQE H2 Simulator

Variational quantum eigensolver for estimating the ground-state energy of molecular hydrogen.

## Overview
- The `H₂` electronic Hamiltonian is reduced to a 2-qubit `Pauli` operator sum:

    `H = c₀ I + c₁ Z₀ + c₂ Z₁ + c₃ Z₀Z₁ + c₄ X₀X₁ + c₅ Y₀Y₁`

- A parameterised `ansatz` prepares a trial quantum state:

    `|ψ(θ)⟩ = CNOT · Ry(θ) |00⟩`

- Expectation values of each `Pauli` term are measured in the appropriate basis

- The weighted sum of expectation values gives an estimate of the molecular `ground-state energy`

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 vqe_h2_simulator.py
```