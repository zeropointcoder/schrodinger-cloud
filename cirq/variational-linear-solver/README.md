# Variational Linear Solver

A minimal variational quantum algorithm that approximates a linear system solution.


## Overview
- We aim to solve a simplified linear system `𝐴𝑥 = 𝑏` by encoding the solution in a quantum state

- A single-qubit variational `ansatz` prepares
    `∣𝜓(𝜃)⟩ = cos⁡(𝜃/2)∣0⟩ + sin⁡(𝜃/2)∣1⟩`

- The probability of measuring `∣1⟩` represents the solution amplitude

- A classical optimiser updates `𝜃` to minimise the cost function
    `𝐶(𝜃) = (𝑃(1)−𝑏)^2`

- Measurements are repeated to obtain `counts`, suitable for `histogram` plotting


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 variational_linear_solver.py
```