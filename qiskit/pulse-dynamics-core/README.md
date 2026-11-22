# [CORE] Pulse Dynamics

Low-level quantum control of a qubit simulated via time-dependent Gaussian pulse dynamics.


## Overview
- Hamiltonian:
    `𝐻(𝑡) = 𝜎𝑧/2 + Ω(𝑡)𝜎𝑥`	​
    with `Ω(𝑡)` as a Gaussian-shaped pulse.

- Simulation: Compute time evolution using `scipy.linalg.expm` at each time step.

- Populations: Track `|0⟩` and `|1⟩` states over time.

- Qiskit Integration: Uses `Statevector` for initialisation and state representation.

- Visualisation: Plots coherent oscillations induced by the pulse.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 pulse_dynamics.py
```