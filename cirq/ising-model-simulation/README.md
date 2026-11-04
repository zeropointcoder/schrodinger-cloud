# Ising Model Simulation

Simulates a small `1D Ising spin` chain with transverse field using quantum circuits.


## Overview
- Each qubit represents a `spin` in the `Ising` model.
- Transverse field rotation: `𝑅𝑥(2ℎ𝑡)` rotates spins around `X-axis`.
- `ZZ` interaction: `𝑒^(−𝑖𝐽𝑡𝑍𝑖(𝑍𝑖+1))` applies Ising interaction between neighbours.
- Measurement: All qubits measured in `Z-basis`; results returned as counts for visualisation.
- **Key formulas**:
    - Transverse rotation: `𝑈ℎ = 𝑒−𝑖ℎ𝑡𝑋`
    - Ising interaction: `𝑈𝐽 = 𝑒^(−𝑖𝐽𝑡𝑍𝑖(𝑍𝑖+1))`


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 ising_model_simulation.py
```