# MaxCut VQE Solver

Solve the MaxCut problem using a Variational Quantum Eigensolver (VQE).

## Overview
- Encode `MaxCut` as a cost `Hamiltonian`
- Build a parameterised quantum circuit `(VQE ansatz)`
- Measure bitstrings and compute expected `cut` value
- Use a `classical` optimiser to minimise energy
- Best parameters approximate the `MaxCut` solution

## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 maxcut_vqe_solver.py
```