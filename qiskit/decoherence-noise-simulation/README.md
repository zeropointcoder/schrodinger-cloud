# Decoherence Noise Simulation

To simulate the effect of `decoherence` using a `noise` model.


## Overview
- Circuit Creation – `One` qubit, apply `Hadamard` gate, then measure.

- Run the circuit on a `noiseless` simulator.

- Add `depolarising` and `amplitude damping` errors to the `Hadamard` gate.

- Plot histograms of `ideal` vs `noisy` results.

- Observe how noise `affects` measurement probabilities.


## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 decoherence_noise_simulation.py
```